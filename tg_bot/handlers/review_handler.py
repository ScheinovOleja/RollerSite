from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from pony.orm import db_session

from tg_bot.models import ReviewsReview, LoginRegisterfrommessangers, OrdersOrder


async def reviews_reg(message: Message, state: FSMContext):
    with db_session:
        text_review = message.text.split('\n', 1)[1]
        num_order = message.text.split(' ', 2)[1].split('\n')[0]
        review = ReviewsReview.get(lambda u: u.order.num_order == num_order)
        if review:
            await message.answer('Вы уже оставили отзыв на этот заказ!\n\nБольше не требуется!)')
        else:
            user = LoginRegisterfrommessangers.get(lambda u: int(u.id_messenger) == message.from_user.id)
            order = OrdersOrder.get(lambda u: u.num_order == num_order)
            if not order:
                await message.answer('Такого заказа не существует!\n\nПроверьте правильность введенного номера заказа '
                                     'и повторите попытку!')
            else:
                ReviewsReview(
                    review=text_review,
                    order=order,
                    user=user.user
                )
                await message.answer('Спасибо за ваш отзыв!\n\nПосле его проверки мы обязательно опубликуем на нашем '
                                     'сайте!')
