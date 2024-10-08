from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ad import Ad

from .base import CRUDBase


class Ad_CRUD(CRUDBase):
    async def get_multi(
            self,
            session: AsyncSession
    ):
        db_objs = await session.execute(select(self.model).order_by(
            self.model.position))
        return db_objs.scalars().all()


ad_crud = Ad_CRUD(Ad)
