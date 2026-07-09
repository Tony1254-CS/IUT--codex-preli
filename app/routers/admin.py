"""Administrative reporting and export endpoints."""
from datetime import date, datetime, time, timedelta

from fastapi import APIRouter, Depends, Query
from fastapi.responses import Response
from sqlalchemy.orm import Session

from .. import cache
from ..auth import require_admin
from ..database import get_db
from ..errors import AppError
from ..models import Booking, Room, User
from ..services.export import generate_export

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/usage-report")
def usage_report(
    frm: date = Query(..., alias="from"),
    to: date = Query(...),
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    # Date string used for cache key
    frm_str = frm.isoformat()
    to_str = to.isoformat()
    cached = cache.get_report(admin.org_id, frm_str, to_str)
    if cached is not None:
        return cached

    range_start = datetime.combine(frm, time.min)
    range_end = datetime.combine(to + timedelta(days=1), time.min)

    rooms = db.query(Room).filter(Room.org_id == admin.org_id).order_by(Room.id.asc()).all()
    room_rows = []
    for room in rooms:
        bookings = (
            db.query(Booking)
            .filter(
                Booking.room_id == room.id,
                Booking.status == "confirmed",
                Booking.start_time >= range_start,
                Booking.start_time < range_end,
            )
            .all()
        )
        room_rows.append(
            {
                "room_id": room.id,
                "room_name": room.name,
                "confirmed_bookings": len(bookings),
                "revenue_cents": sum(b.price_cents for b in bookings),
            }
        )

    result_dict = {
        "from": frm_str,
        "to": to_str,
        "rooms": room_rows,
    }
    cache.set_report(admin.org_id, frm_str, to_str, result_dict)
    return result_dict


@router.get("/export")
def export(
    room_id: int | None = Query(None),
    include_all: bool = Query(False),
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    if room_id is not None:
        room = db.query(Room).filter(Room.id == room_id, Room.org_id == admin.org_id).first()
        if room is None:
            raise AppError(404, "ROOM_NOT_FOUND", "Room not found")
    csv_body = generate_export(db, admin.org_id, admin.id, room_id, include_all)
    return Response(content=csv_body, media_type="text/csv")
