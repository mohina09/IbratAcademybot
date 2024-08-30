from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, CallbackQuery
from keyboards.inline.inline_keyboards import back_btn, back2_btn, back3_btn, back_3_btn, back_3_2_btn, back4_btn, back_4_btn, back_4_2_btn, back_4_3_btn, back5_btn, back_5_btn, back_5_2_btn, back_5_3_btn, back_5_4_btn, back_5_5_btn, back_5_6_btn, back_5_7_btn, back_5_8_btn, back_5_9_btn, back_5_10_btn
from loader import dp, bot
from filters.private_filter import IsPrivate


@dp.message_handler(IsPrivate(), content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(IsPrivate(), content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.callback_query_handler(text="beginner1")
async def beginner_1(call: types.CallbackQuery):
    beginner1 = "BAACAgQAAxkBAANdZsW_bs0Rj48NEQH43AbD490e0B0AAgz4AAIyZBlTfvV2kEe1EY41BA"
    await call.message.delete()
    await call.message.answer_video(video=beginner1, caption="""🔘Alifbo""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner2")
async def beginner_2(call: types.CallbackQuery):
    beginner2 = "BAACAgQAAxkBAANyZsXC4wUmTMurhg90LjaiTA2VfJAAAuH4AAIyZBlTgW5m4x48Q_o1BA"
    await call.message.delete()
    await call.message.answer_video(video=beginner2, caption="""🔘To Be Verb""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner3")
async def beginner_3(call: types.CallbackQuery):
    beginner3 = "BAACAgQAAxkBAAOEZsXEJ-Vk4MFYHqJ84CFVoXMcy6kAAl7-AAIyZBlTf7MpC7Qtufk1BA"
    await call.message.delete()
    await call.message.answer_video(video=beginner3, caption="""🔘To be verb|Question forms""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner4")
async def beginner_4(call: types.CallbackQuery):
    beginner4 = "BAACAgQAAxkBAAOYZsXIM6LEP0Dh5j_VJbEdewFvsZsAAtcBAQABMmQZUzoPvNy3dw8kNQQ"
    await call.message.delete()
    await call.message.answer_video(video=beginner4, caption="""🔘Present Continuos Tense""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner5")
async def beginner_5(call: CallbackQuery):
    beginner5 = "BAACAgQAAxkBAAOaZsXI_A8eH4sX8ba7CNAJryzHNZEAAgQBAQABMmQZUw58qIR8h_EBNQQ"
    await call.message.delete()
    await call.message.answer_video(video=beginner5, caption="""🔘Present Continuous Questions.""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner6")
async def beginner_6(call: types.CallbackQuery):
    beginner6 = "BAACAgQAAxkBAAOcZsXJJE0mAR0FQw7bJA0v6m_IOrEAAokCAQABMmQZU6YXTBsdludHNQQ"
    await call.message.delete()
    await call.message.answer_video(video=beginner6, caption="""🔘Present Simple Tense""", reply_markup=back_btn)



@dp.callback_query_handler(text="beginner7")
async def beginner_7(call: types.CallbackQuery):
    beginner7 = "BAACAgQAAxkBAAOeZsXW334qGI_394JegupHUYG4gcoAAnMKAQABMmQZU5Jy3oB7q7z6NQQ"
    await call.message.delete()
    await call.message.answer_video(video=beginner7, caption="""🔘Present Simple Negative""", reply_markup=back_btn)


@dp.callback_query_handler(text="beginner8")
async def beginner_8(call: types.CallbackQuery):
    beginner8 = "BAACAgQAAxkBAAOgZsXW9wT_q8XI_LVeDafdi_sSBYIAAv8KAQABMmQZUwkCdW1BNxZkNQQ"
    await call.message.delete()
    await call.message.answer_video(video=beginner8, caption="""🔘Present Simple Questions""", reply_markup=back_btn)


@dp.callback_query_handler(text="elementry1")
async def elementry_1(call: types.CallbackQuery):
    elementry1 = "BAACAgQAAxkBAAPYZsYb1yofwfjp1_Du56AbM8PeY7kAAt8GAQABMmQZUx-QqPVWn9xYNQQ"
    await call.message.delete()
    await call.message.answer_video(video=elementry1, caption="""🔘Present Simple and Present Continuous""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry2")
async def elementry_2(call: types.CallbackQuery):
    elementry2 = "BAACAgQAAxkBAAPaZsYfrXz_bL_yQ6QAAbGMblI-XQ8GAAJrbAEAAbALMVMJIOV80kyY8TUE"
    await call.message.delete()
    await call.message.answer_video(video=elementry2, caption="""🔘I have got ... and I have ...""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry3")
async def elementry_3(call: CallbackQuery):
    elementry3 = "BAACAgQAAxkBAAPcZsYiCsDpOrSLTIRa9NK08ySpdEYAAmFtAQABsAsxUz2DKjSn_geENQQ"
    await call.message.delete()
    await call.message.answer_video(video=elementry3, caption="""🔘Past Simple""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry4")
async def elementry_4(call: CallbackQuery):
    elementry4 = "BAACAgQAAxkBAAPpZsYx8_VlnSV18Pr4wctgrrndf5YAAlVvAQABsAsxUwy1eiWqTs9kNQQ"
    await call.message.delete()
    await call.message.answer_video(video=elementry4, caption="""🔘Past Simple 2""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry5")
async def elementry_5(call: CallbackQuery):
    elementry5 = "BAACAgQAAxkBAAIBL2bG1RbIb-03ESoOj8yJygbTlA09AAI0agEAAbALMVMHZHTmyWj7JzUE"
    await call.message.delete()
    await call.message.answer_video(video=elementry5, caption="""🔘Past Simple Negative and Questions""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry6")
async def elementry_6(call: CallbackQuery):
    elementry6 = "BAACAgQAAxkBAAIBQmbHTyJvQ6O8Iz8LS9IBL_aMloSeAAI5cgEAAbALMVOQZ0EFLC9ZJzUE"
    await call.message.delete()
    await call.message.answer_video(video=elementry6, caption="""🔘Past Continuous""", reply_markup=back2_btn)


@dp.callback_query_handler(text="elementry7")
async def elementry_7(call: CallbackQuery):
    elementry7 = "BAACAgQAAxkBAAIBRmbHTzbcNkkWjeGtvc8bkVbeSQrCAAKOcgEAAbALMVOsk6ZNcB3llTUE"
    await call.message.delete()
    await call.message.answer_video(video=elementry7, caption="""🔘Past Simple and Past Continuous""", reply_markup=back2_btn)


@dp.callback_query_handler(text="pre_intermediate1")
async def pre_intermediate_1(call: CallbackQuery):
    pre_intermediate1 = "BAACAgQAAxkBAAIBa2bHYgrx2C1s3OXTRObpiRVPTVsmAAImcwEAAbALMVO4lyVoB_OfjzUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate1, caption="""Present Perfect""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate2")
async def pre_intermediate_2(call: CallbackQuery):
    pre_intermediate2 = "BAACAgQAAxkBAAIBbWbHYjTMV1M2m7Tyw8UtLaYAAZrsMAAC1nMBAAGwCzFTBLlIihK3LWY1BA"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate2, caption="""Present Perfect 2""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate3")
async def pre_intermediate_3(call: CallbackQuery):
    pre_intermediate3 = "BAACAgQAAxkBAAIBb2bHYlRTvxfWRbr8zzG1VsBDssG1AAJVdQEAAbALMVMmLKI4uKRamjUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate3, caption="""Present Perfect 3""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate4")
async def pre_intermediate_4(call: CallbackQuery):
    pre_intermediate4 = "BAACAgQAAxkBAAIBcWbHYntVIYsAAXE4hO8O6dV03vbbvgACJnYBAAGwCzFTIaQU4xzR4bg1BA"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate4, caption="""Present Perfect""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate5")
async def pre_intermediate_5(call: CallbackQuery):
    pre_intermediate5 = "BAACAgQAAxkBAAIBc2bHYvyqgvmLPMHgPE4IG4LJoAzDAAK7iQEAAbALMVMPm2bEMD9qszUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate5, caption="""Since/For/Ago""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate6")
async def pre_intermediate_6(call: CallbackQuery):
    pre_intermediate6 = "BAACAgQAAxkBAAIBdWbHYyPkvfCOI6oRZq-8i2IX5D_IAAJ7igEAAbALMVPbpfH9kp2vXTUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate6, caption="""Present Perfect and Past Simple""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate7")
async def pre_intermediate_7(call: CallbackQuery):
    pre_intermediate7 = "BAACAgQAAxkBAAIBd2bHY0ZRAZmGkVjwo7oWx18_UW-sAAJQiwEAAbALMVPKIuf3Z-ZjxTUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate7, caption="""Passive voice""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate8")
async def pre_intermediate_8(call: CallbackQuery):
    pre_intermediate8 = "BAACAgQAAxkBAAIBeWbHY241MjK7vwsY_ZVCcPPKwN4AA1iLAQABsAsxUxwfyTzuJP8rNQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate8, caption="""Passive voice 2""", reply_markup=back3_btn)


@dp.callback_query_handler(text="pre_intermediate9")
async def pre_intermediate_9(call: CallbackQuery):
    pre_intermediate9 = "BAACAgQAAxkBAAIBfWbHY51PpKP-6j7sPGq_YBjM7iPKAALqiwEAAbALMVPqSHiVpdX53jUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate9, caption="""Present and Past tenses""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate10")
async def pre_intermediate_10(call: CallbackQuery):
    pre_intermediate10 = "BAACAgQAAxkBAAIBe2bHY42GUeXxTkB1hRyQjmN-yQ1wAAJtjAEAAbALMVOg4Qtoj9cJBzUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate10, caption="""Regular and Irregular verbes""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate11")
async def pre_intermediate_11(call: CallbackQuery):
    pre_intermediate11 = "BAACAgQAAxkBAAIBf2bHZCfVRp_Z7rHTW98Cmii0ogI6AAI0jQEAAbALMVMYu0OGLlSYwjUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate11, caption="""Used to ...""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate12")
async def pre_intermediate_12(call: CallbackQuery):
    pre_intermediate12 = "BAACAgQAAxkBAAIBg2bHZMfpjROzPzK7IVgeJdYxEJziAALOjQEAAbALMVNdYoMMrmT5ljUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate12, caption="""What are you doing tommorrow?""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate13")
async def pre_intermediate_13(call: CallbackQuery):
    pre_intermediate13 = "BAACAgQAAxkBAAIBg2bHZMfpjROzPzK7IVgeJdYxEJziAALOjQEAAbALMVNdYoMMrmT5ljUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate13, caption="""I am going to""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate14")
async def pre_intermediate_14(call: CallbackQuery):
    pre_intermediate14 = "BAACAgQAAxkBAAIBhWbHZWQiFnbPq-YI5hO9UWa2jumoAAJskAEAAbALMVMqJau6HhZA-jUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate14, caption="""Future tenses:
Biz "will"ni kelajak zamon uchun ishlatamiz.

Rule: Ammo biz "will"ni aniq rejalashtirilgan ish-harakatlar uchun ishlata olmaymiz.

You can say I shall(=I will) and we shall(=we will)
Rule: But do not use shall with you/they/he/she/it""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate15")
async def pre_intermediate_15(call: CallbackQuery):
    pre_intermediate15 = "BAACAgQAAxkBAAIBiWbHZdS3g5tez6Wd1fUMj1PnbiizAAKNowACmNhRUwqB5GzA8lmeNQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate15, caption="""Future tenses 2""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate16")
async def pre_intermediate_16(call: CallbackQuery):
    pre_intermediate16 = "BAACAgQAAxkBAAIBh2bHZcM3QNImxdRpdt1-Pm39Rtt0AAIXrAACmNhRU58JRc3rHOSANQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate16, caption="""Modal verbs""", reply_markup=back_3_btn)


@dp.callback_query_handler(text="pre_intermediate17")
async def pre_intermediate_17(call: CallbackQuery):
    pre_intermediate17 = "BAACAgQAAxkBAAIBi2bHZgNA7Q6rcCAqe2gHYNmy48tNAALarwACmNhRU9cH7z-S_QHVNQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate17, caption="""Modal verbs 2""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate18")
async def pre_intermediate_18(call: CallbackQuery):
    pre_intermediate18 = "BAACAgQAAxkBAAIBjWbHZihUKz7yMaKZwxrLAefAQ3VrAAIVtQACmNhRU8lmtBvQqGDANQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate18, caption="""Modal verbs 3""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate19")
async def pre_intermediate_19(call: CallbackQuery):
    pre_intermediate19 = "BAACAgQAAxkBAAIBj2bHZvEfu9X4HVLS4FAmXTsJ9lVtAAKAtQACmNhRU2SFJVNV8EytNQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate19, caption="""Modal verbs 4""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate20")
async def pre_intermediate_20(call: CallbackQuery):
    pre_intermediate20 = "BAACAgQAAxkBAAIBkWbHZw2jJu6PdVEyQ8uklvve0LG2AALK-wACmNhRU7d4tr18R6n2NQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate20, caption="""I have to ...""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate21")
async def pre_intermediate_21(call: CallbackQuery):
    pre_intermediate21 = "BAACAgQAAxkBAAIBk2bHZy1pylUMzTYoEEPtB2iSflZ0AAP8AAKY2FFT_kSN0gxc2Ho1BA"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate21, caption=""" Would you like to ...""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate22")
async def pre_intermediate_22(call: CallbackQuery):
    pre_intermediate22 = "BAACAgQAAxkBAAIBlWbHZ0rTju_Pg5Eu7cD3AgHQHQOmAALWCAEAAZjYUVMxh8LOPVbLVTUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate22, caption="""There is vs There are""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate23")
async def pre_intermediate_23(call: CallbackQuery):
    pre_intermediate23 = "BAACAgQAAxkBAAIBl2bHZ3AwiV_7xcYrfR1LoMm2w99JAALA_AACmNhRU1RstmQZkKUzNQQ"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate23, caption="""There was vs There were""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="pre_intermediate24")
async def pre_intermediate_24(call: CallbackQuery):
    pre_intermediate24 = "BAACAgQAAxkBAAIBmWbHZ43s9cAHjPstroLXzX8LP7QoAAIhCAEAAZjYUVNlvobDvGor0TUE"
    await call.message.delete()
    await call.message.answer_video(video=pre_intermediate24, caption="""It ...""", reply_markup=back_3_2_btn)


@dp.callback_query_handler(text="intermediate1")
async def intermediate_1(call: CallbackQuery):
    intermediate1 = "BAACAgQAAxkBAAIBumbIZjV54vT6oJQQ0drdydhWJK2tAAIeDgEAAZjYUVMz2c0LqdjFbjUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate1, caption="""I'm vs I do""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate2")
async def intermediate_2(call: CallbackQuery):
    intermediate2 = "BAACAgQAAxkBAAIBvGbIZkUo78eoQ8HEAvrPbUxSbm4oAAKAPwEAAZjYUVN-uoX-PeNJaTUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate2, caption="""Question forms of all tenses""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate3")
async def intermediate_3(call: CallbackQuery):
    intermediate3 = "BAACAgQAAxkBAAIBvmbIZlnqDFc-BOnYGR3rdnc-aHmdAAKbQAEAAZjYUVMYYZ6AYLI49zUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate3, caption="""Too/either/neither do/So am I""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate4")
async def intermediate_4(call: CallbackQuery):
    intermediate4 = "BAACAgQAAxkBAAIBwGbIZm46UXLllgXPMJYL4_S90A5NAAILQQEAAZjYUVPcOpDX8iDEFzUEb"
    await call.message.delete()
    await call.message.answer_video(video=intermediate4, caption="""Haven't/Don't/Isn't""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate5")
async def intermediate_5(call: CallbackQuery):
    intermediate5 = "BAACAgQAAxkBAAIBwmbIZqFAQeKivrTzsDbDqhS0lLHZAAJPTAIAAZjYUVPzdwGsfEgk5TUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate5, caption="""Have you ... ?/ Do they ... ?""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate6")
async def intermediate_6(call: CallbackQuery):
    intermediate6 = "BAACAgQAAxkBAAIBxmbIZsgrPNfbF5-_SdSWOyeOiXv-AAI0UQIAAZjYUVM9IZye9DdEVjUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate6, caption="""Who saw you? vs Who did you see?""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate7")
async def intermediate_7(call: CallbackQuery):
    intermediate7 = "BAACAgQAAxkBAAIByGbIZtyQyL623V9YEDSyqzZfs_LRAAIWNQEAAbjFWFOvSXZTwaNMFTUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate7, caption="""Who say you vs Who did you see""", reply_markup=back4_btn)


@dp.callback_query_handler(text="intermediate8")
async def intermediate_8(call: CallbackQuery):
    intermediate8 = "BAACAgQAAxkBAAIBymbIZvCcXGVz4ZhVO443D6AfS-v7AAIIRgEAAbjFWFOt3n-meX8b6DUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate8, caption="""What is it like?""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate9")
async def intermediate_9(call: CallbackQuery):
    intermediate9 = "BAACAgQAAxkBAAIBzmbIZw3Q7L24FAS5BpALn06rXW7sAAJdRwEAAbjFWFOttHYpFZB5xDUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate9, caption="""What? / Which? / How?""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate10")
async def intermediate_10(call: CallbackQuery):
    intermediate10 = "BAACAgIAAxkBAAIBzGbIZwG34lSZMufA_5EUO4MeRcV-AAL4MgAC9AlYS3kZMWtflVW7NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate10, caption="""How does it take?""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate11")
async def intermediate_11(call: CallbackQuery):
    intermediate11 = "BAACAgIAAxkBAAIB0GbIZ0a6K0hzd-3dqkn-JLaN6FpsAAL9MgAC9AlYSzWzCiH-DqN3NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate11, caption="""Do you know where ... ?""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate12")
async def intermediate_12(call: CallbackQuery):
    intermediate12 = "BAACAgIAAxkBAAIB0mbIZ1bi-MoSwjA_a-8P-O0ldI1lAAL5MgAC9AlYS8B5Ogp8NYNjNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate12, caption="""She said that""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate13")
async def intermediate_13(call: CallbackQuery):
    intermediate13 = "BAACAgIAAxkBAAIB1GbIZ331iJQK454tTnwgx-dCDla4AAIDMwAC9AlYS_SYQVbrHCZrNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate13, caption="""Work vs working""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate14")
async def intermediate_14(call: CallbackQuery):
    intermediate14 = "BAACAgQAAxkBAAIB1mbIZ5XL9CS2DlS64Lj9Aknw0OuPAAK0SgEAAbjFWFM8tw6SHoDR1TUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate14, caption="""I want to do vs I enjoy doing""", reply_markup=back_4_btn)


@dp.callback_query_handler(text="intermediate15")
async def intermediate_15(call: CallbackQuery):
    intermediate15 = "BAACAgIAAxkBAAIB2GbIZ6MDHy8k6JShsXypoYil4BdWAAIJMwAC9AlYS3CvF7jqU6qGNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate15, caption="""I told you to ...""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate16")
async def intermediate_16(call: CallbackQuery):
    intermediate16 = "BAACAgIAAxkBAAIB2mbIZ7lkIRCaTxXPMo0qashWt7zKAAIMMwAC9AlYS-IpzC4AAfcY3TUE"
    await call.message.delete()
    await call.message.answer_video(video=intermediate16, caption="""I went to the shop to ...""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate17")
async def intermediate_17(call: CallbackQuery):
    intermediate17 = "BAACAgIAAxkBAAIB3GbIZ8_uAnEti2uN8Q8RMG1jIZdLAAIRMwAC9AlYSySQHusFv7ZhNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate17, caption="""Go to / Go on / Go for""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate18")
async def intermediate_18(call: CallbackQuery):
    intermediate18 = "BAACAgIAAxkBAAIB3mbIZ-CIZY-Dw3WLXkT4r3OG1G3lAAIUMwAC9AlYS0tq7yKX59uNNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate18, caption="""Get a letter / Get a job""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate19")
async def intermediate_19(call: CallbackQuery):
    intermediate19 = "BAACAgIAAxkBAAIB4GbIZ_UahqnjeUN8gVvhR6GvlRxSAAIWMwAC9AlYS0hirjr2D3h-NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate19, caption="""Do vs Make""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate20")
async def intermediate_20(call: CallbackQuery):
    intermediate20 = "BAACAgIAAxkBAAIB4mbIaAu4oJb-_4VecHqpYYoK_RRbAAIXMwAC9AlYS_kDgjQsw1FtNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate20, caption="""Have or Have got""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate21")
async def intermediate_21(call: CallbackQuery):
    intermediate21 = "BAACAgIAAxkBAAIB5GbIaCuM0XbbC19NE2kbvtUGk1NEAAIZMwAC9AlYS0Lvp-wzwsGtNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate21, caption="""Pronouns""", reply_markup=back_4_2_btn)


@dp.callback_query_handler(text="intermediate22")
async def intermediate_22(call: CallbackQuery):
    intermediate22 = "BAACAgIAAxkBAAIB5mbIaD4RBwdBarfNmFY-ZVOpabWLAAIaMwAC9AlYS3P8iuUK_AWTNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate22, caption="""Pronouns 2""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate23")
async def intermediate_23(call: CallbackQuery):
    intermediate23 = "BAACAgIAAxkBAAIB6GbIaFgh55__imAtPlfg5LN_IZHBAAIbMwAC9AlYS9YaqBTViL16NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate23, caption="""Pronouns 3""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate24")
async def intermediate_24(call: CallbackQuery):
    intermediate24 = "BAACAgIAAxkBAAIB6mbIaG0l3RqNyO1xSSfQ4rCHsYoWAAJHMwAC9AlYS_4pAcTZkuT7NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate24, caption="""Pronouns 4""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate25")
async def intermediate_25(call: CallbackQuery):
    intermediate25 = "BAACAgIAAxkBAAIB7GbIaIKeJWmr0rOiiSMpwsaUBNAwAAJKMwAC9AlYS3VJf75gQIH4NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate25, caption="""-ning kelishik qo'shimchasi""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate26")
async def intermediate_26(call: CallbackQuery):
    intermediate26 = "BAACAgIAAxkBAAIB7mbIaJwPD8ObsDlj9X4Ox75syfU9AAJLMwAC9AlYSxyPoyvcLc4YNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate26, caption="""A and an articles""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate27")
async def intermediate_27(call: CallbackQuery):
    intermediate27 = "BAACAgIAAxkBAAIB8GbIaLctWLdwHPgaQeXs_A9Of1AOAAJNMwAC9AlYS8aWk358TVuvNQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate27, caption="""Singular and Plural nouns""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="intermediate28")
async def intermediate_28(call: CallbackQuery):
    intermediate28 = "BAACAgIAAxkBAAIB8mbIaMpDSO4l4sOsJ-AEzt9lhr48AAJOMwAC9AlYS6u3lGvrcvr3NQQ"
    await call.message.delete()
    await call.message.answer_video(video=intermediate28, caption="""Countable and Uncountable nouns""", reply_markup=back_4_3_btn)


@dp.callback_query_handler(text="upper_intermediate1")
async def upper_intermediate_1(call: CallbackQuery):
    upper_intermediate1 = "BAACAgIAAxkBAAIChmbJ9c0SuMsqDtscs20gi8AdS8YGAAJRMwAC9AlYS1CpbfUPLNJ2NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate1, caption="""A vs The Articles""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate2")
async def upper_intermediate_2(call: CallbackQuery):
    upper_intermediate2 = "BAACAgIAAxkBAAICiGbJ9gz4cZ7iAlEyCVcMg6rOCigbAAJXMwAC9AlYSwzY8G1fMqIuNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate2, caption="""The article""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate3")
async def upper_intermediate_3(call: CallbackQuery):
    upper_intermediate3 = "BAACAgIAAxkBAAICimbJ9lZvQ7fvJT0ak8G0T5KYVIarAAJSMwAC9AlYS9F1ILxzPj2INQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate3, caption="""Go to work vs Go home""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate4")
async def upper_intermediate_1(call: CallbackQuery):
    upper_intermediate1 = "BAACAgIAAxkBAAICjGbJ9nnqS4ljli8ZCGF2IdXKfm0nAAIXOwACkMppSwct2KnesSdPNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate1, caption="""When NOT to use "the" """, reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate5")
async def upper_intermediate_1(call: CallbackQuery):
    upper_intermediate1 = "BAACAgIAAxkBAAICjmbJ9qznaCQCjhs5qew-9aJb5lPyAAIZOwACkMppS_rHh9HlrnNKNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate1, caption="""Names of places""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate6")
async def upper_intermediate_6(call: CallbackQuery):
    upper_intermediate6 = "BAACAgIAAxkBAAICkGbJ9szyVapgPD8GRSqqck-dBWuZAAIcOwACkMppS06iydnMgb1UNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate6, caption="""This/That/Those/These""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate7")
async def upper_intermediate_7(call: CallbackQuery):
    upper_intermediate7 = "BAACAgIAAxkBAAICkmbJ9vvwdjX1sPwakvVcyO2Y1dFrAAIfOwACkMppS-g6CixmdNX8NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate7, caption="""One vs Ones""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate8")
async def upper_intermediate_8(call: CallbackQuery):
    upper_intermediate8 = "BAACAgIAAxkBAAIClGbJ9wfza689JWpQb266khsxiYauAAIkOwACkMppS6HFYMUcv_SbNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate8, caption="""Some vs Any:""", reply_markup=back5_btn)


@dp.callback_query_handler(text="upper_intermediate9")
async def upper_intermediate_9(call: CallbackQuery):
    upper_intermediate9 = "BAACAgIAAxkBAAIClmbJ9xIoAdSsNCniFeoQuKtTrBiOAAIlOwACkMppS5xx22G_TMS7NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate9, caption="""No + any/No/None:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate10")
async def upper_intermediate_10(call: CallbackQuery):
    upper_intermediate10 = "BAACAgIAAxkBAAICmGbJ92XIqZ7e5z2yG4SUIloUVRS3AAIqOwACkMppS8dKe1u9jkVxNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate10, caption="""Not+anybody vs Nobody:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate11")
async def upper_intermediate_11(call: CallbackQuery):
    upper_intermediate11 = "BAACAgIAAxkBAAICmmbJ941UTepgWdzOM1EAAVkjTEqCfgACLTsAApDKaUtfBkXwwp9x2zUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate11, caption="""Somebody/Anything/Nowhere:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate12")
async def upper_intermediate_12(call: CallbackQuery):
    upper_intermediate12 = "BAACAgIAAxkBAAICnGbJ96Zp1snZq4EJNIXZ19hny8-HAAIvOwACkMppSxm9DNY3AXXzNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate12, caption="""Every vs All:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate13")
async def upper_intermediate_13(call: CallbackQuery):
    upper_intermediate13 = "BAACAgIAAxkBAAICnmbJ971awzitvk74gwAB08FdxCixDgACMDsAApDKaUu3Qk7BxlQbrzUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate13, caption="""All/Most/Some/Any:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate14")
async def upper_intermediate_14(call: CallbackQuery):
    upper_intermediate14 = "BAACAgIAAxkBAAICoGbJ9-9qvIMk16pZAaiOQruhku9vAAK_NwACPXV4S9x7tJcOODTJNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate14, caption="""Both/Either/Neither:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate15")
async def upper_intermediate_15(call: CallbackQuery):
    upper_intermediate15 = "BAACAgIAAxkBAAICombJ9_g5K422NHSFglgx5M0zP590AALANwACPXV4Sx8PkmIjvFhUNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate15, caption="""A lot/much/many:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate16")
async def upper_intermediate_16(call: CallbackQuery):
    upper_intermediate16 = "BAACAgIAAxkBAAICpGbJ-CFQv75vhbU92caxze3ejz4zAALBNwACPXV4S92ygCbGUQvkNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate16, caption="""A little vs A few:""", reply_markup=back_5_btn)


@dp.callback_query_handler(text="upper_intermediate17")
async def upper_intermediate_17(call: CallbackQuery):
    upper_intermediate17 = "BAACAgIAAxkBAAICpmbJ-CtoN-bZj2338rbumRezTUQZAALCNwACPXV4S4WNByOlkj-TNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate17, caption="""Adjectives:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate18")
async def upper_intermediate_18(call: CallbackQuery):
    upper_intermediate18 = "BAACAgIAAxkBAAICqGbJ-DdseX5naDqeNDi9nNOQHk23AALENwACPXV4S9PTbtYkvyhBNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate18, caption="""Adverbs:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate19")
async def upper_intermediate_19(call: CallbackQuery):
    upper_intermediate19 = "BAACAgIAAxkBAAICqmbJ-Rj4-Zwr7zFEbc-Rs6nLjpVuAALlLwACUHSIS8k0sSrJzIHYNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate19, caption="""Old vs older:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate20")
async def upper_intermediate_20(call: CallbackQuery):
    upper_intermediate20 = "BAACAgIAAxkBAAICrGbJ-T0aFjuElURZ6yjT7UwjkV37AALpLwACUHSISzuSTzGnXThfNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate20, caption="""Older/More expensive than ...:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate21")
async def upper_intermediate_21(call: CallbackQuery):
    upper_intermediate21 = "BAACAgIAAxkBAAICsGbJ-UYdRd_s8wABVLwc6p277WXQ0gAC-C8AAlB0iEvg8fxLKgT4zTUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate21, caption="""Not as ... as:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate22")
async def upper_intermediate_22(call: CallbackQuery):
    upper_intermediate22 = "BAACAgIAAxkBAAICsmbJ-XenKuWpfknjwV7Bw-wVErXBAAL6LwACUHSIS3XChZBnX2mLNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate22, caption="""The oldest/The most expensive:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate23")
async def upper_intermediate_23(call: CallbackQuery):
    upper_intermediate23 = "BAACAgIAAxkBAAICtGbJ-Y06tdSeBeCi2XTBoswwJFzrAAL8LwACUHSIS6E8vjaTklMjNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate23, caption="""Enough:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate24")
async def upper_intermediate_24(call: CallbackQuery):
    upper_intermediate24 = "BAACAgIAAxkBAAICtmbJ-aZTj7OVWBsCHg5ds5MFieRCAAKfOAACvVWYS8YhjobiXL6INQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate24, caption="""Too:""", reply_markup=back_5_2_btn)


@dp.callback_query_handler(text="upper_intermediate25")
async def upper_intermediate_25(call: CallbackQuery):
    upper_intermediate25 = "BAACAgIAAxkBAAICuGbJ-diC07lfRPGNrcd1toxkW3xMAAKgOAACvVWYS6sSOUTs24c4NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate25, caption="""Word order:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate26")
async def upper_intermediate_26(call: CallbackQuery):
    upper_intermediate26 = "BAACAgIAAxkBAAICumbJ-fNtiBWtdYu0TjE8fqIQ9_HuAAKhOAACvVWYS_wD4sjY5t6oNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate26, caption="""Word order 2:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate27")
async def upper_intermediate_27(call: CallbackQuery):
    upper_intermediate27 = "BAACAgIAAxkBAAICvGbJ-j4uokbWdVS144WN71QM6z7KAAKjOAACvVWYS8zG6_RXXD9-NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate27, caption="""Still vs Yet:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate28")
async def upper_intermediate_28(call: CallbackQuery):
    upper_intermediate28 = "BAACAgIAAxkBAAICvmbJ-kZTVGgekbDLom564CY83LgzAAKkOAACvVWYSwKpqSs82gvyNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate28, caption="""Give me .../ Give it to:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate29")
async def upper_intermediate_29(call: CallbackQuery):
    upper_intermediate29 = "BAACAgIAAxkBAAICwGbJ-lGXR-hWOC_CimWLdlD1MgQMAAKIOAAC8SewS61i-hhBykuSNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate29, caption="""At/On/In:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate30")
async def upper_intermediate_30(call: CallbackQuery):
    upper_intermediate30 = "BAACAgIAAxkBAAICwmbJ-lv8rnZPICNcvqSHuttJ-xTUAAKJOAAC8SewS_m-2-SG2cybNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate30, caption="""From... to, Until, Since, For:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate31")
async def upper_intermediate_31(call: CallbackQuery):
    upper_intermediate31 = "BAACAgIAAxkBAAICxGbJ-mVrwt1f0DgPvcx_isMlxiRNAAKKOAAC8SewSy5WXeNpaOwxNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate31, caption="""Before, After, During, While:""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate32")
async def upper_intermediate_32(call: CallbackQuery):
    upper_intermediate32 = "BAACAgIAAxkBAAICxmbJ-nPpSb6nE5uvFDYcTROI6D3JAAKMOAAC8SewSwmhgkTIHumXNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate32, caption="""In/At (Places)""", reply_markup=back_5_3_btn)


@dp.callback_query_handler(text="upper_intermediate33")
async def upper_intermediate_33(call: CallbackQuery):
    upper_intermediate33 = "BAACAgIAAxkBAAICyGbJ-n8gF8Rz2_aWfIN0ljVkxqAWAAKOOAAC8SewS9O_7QISRWh2NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate33, caption="""In/At/On (places 2):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate34")
async def upper_intermediate_34(call: CallbackQuery):
    upper_intermediate34 = "BAACAgIAAxkBAAICymbJ-7fgEuTP-jsEtExRIxEfu5t5AAKQOAAC8SewS3zXzNhFkWWiNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate34, caption="""In/At/On (places 3):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate35")
async def upper_intermediate_35(call: CallbackQuery):
    upper_intermediate35 = "BAACAgIAAxkBAAICzGbJ-8E8SCoPBCjFmAOxDvpy31bqAAKSOAAC8SewS2SUVSzl8CcONQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate35, caption="""On/Under/Behind (prepositions):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate36")
async def upper_intermediate_36(call: CallbackQuery):
    upper_intermediate36 = "BAACAgIAAxkBAAICzmbJ-8xRS1IeuwX9TT0HAVyY6A-RAAKTOAAC8SewSwQRFPkbw1MAATUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate36, caption="""Up/Over/Through (prepositions):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate37")
async def upper_intermediate_37(call: CallbackQuery):
    upper_intermediate37 = "BAACAgIAAxkBAAIC0GbJ-9emYCUhAAEwet43Blj_MO1fqQAClDgAAvEnsEsGJL4jO20gjjUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate37, caption="""At/By/With/Without/About (prepositions):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate38")
async def upper_intermediate_38(call: CallbackQuery):
    upper_intermediate38 = "BAACAgIAAxkBAAIC0mbJ--itT204L10YunRe77hU-2WsAAKVOAAC8SewS9Cp9AiPXy_BNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate38, caption="""Afraid of... / On holiday (word + prpositions):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate39")
async def upper_intermediate_39(call: CallbackQuery):
    upper_intermediate39 = "BAACAgIAAxkBAAIC1GbJ-_POnGn8m5Lix1ddz2M59vjmAAIgNwACM8oYSKQCy50oAx9dNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate39, caption="""Look at / Listen to (verb + prepostions):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate40")
async def upper_intermediate_40(call: CallbackQuery):
    upper_intermediate40 = "BAACAgIAAxkBAAIC1mbJ_AK3kyELUapguYBK4l-KiwJNAAIiNwACM8oYSEi--98dZk4tNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate40, caption="""Go in / Fall off / Run away (phrasal verb 1):""", reply_markup=back_5_4_btn)


@dp.callback_query_handler(text="upper_intermediate41")
async def upper_intermediate_41(call: CallbackQuery):
    upper_intermediate41 = "BAACAgIAAxkBAAIC2GbJ_A84NBWhYbMXe4DugywXJ6MTAAIkNwACM8oYSCPv-XUVPZ8MNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate41, caption="""Put on your shoes / Put your shoes on  (phrasal verb 1):""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate42")
async def upper_intermediate_42(call: CallbackQuery):
    upper_intermediate42 = "BAACAgIAAxkBAAIC2mbJ_BqRsl75TBUisPFzmR2cE4PQAAIlNwACM8oYSEikWUn6G9V9NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate42, caption="""And / But / Or / So / Because:""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate43")
async def upper_intermediate_43(call: CallbackQuery):
    upper_intermediate43 = "BAACAgIAAxkBAAIC3GbJ_CS3IJplwTjYpmtsfqyN_u9EAAImNwACM8oYSDwGBOQV-9cfNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate43, caption="""When?:""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate44")
async def upper_intermediate_44(call: CallbackQuery):
    upper_intermediate44 = "BAACAgIAAxkBAAIC3mbJ_C1fQ5f952omeF_sAAGtVLNFugACKDcAAjPKGEil42GxbGwEMDUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate44, caption="""If we go ... If you see ...:""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate45")
async def upper_intermediate_45(call: CallbackQuery):
    upper_intermediate45 = "BAACAgIAAxkBAAIC4GbJ_DftdKepjehZfxvlvN1uyfZGAAIqNwACM8oYSIm3K79ozYuZNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate45, caption="""If I had... If we went...:""", reply_markup=vzback_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate46")
async def upper_intermediate_46(call: CallbackQuery):
    upper_intermediate46 = "BAACAgIAAxkBAAIC4mbJ_GU8qOaNGTqqNokik3y_ltPAAAItNwACM8oYSBrNcg4JGvvhNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate46, caption="""A person who ...  a thing that/which (relative clauses 1):""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate47")
async def upper_intermediate_47(call: CallbackQuery):
    upper_intermediate47 = "BAACAgIAAxkBAAIC5GbJ_jNGTKrDqr8iBlRcu0KPIzc8AAIuNwACM8oYSCVyfVuVhKUzNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate47, caption="""The people we met the hotel you stayed at:""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate48")
async def upper_intermediate_48(call: CallbackQuery):
    upper_intermediate48 = "BAACAgIAAxkBAAIC5mbJ_kgb05mgw9EyOMhyAqbT6SLBAAI1NwACM8oYSHBhU95Xk-cBNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate48, caption="""Can\could and (be) able to:""", reply_markup=back_5_5_btn)


@dp.callback_query_handler(text="upper_intermediate49")
async def upper_intermediate_49(call: CallbackQuery):
    upper_intermediate49 = "BAACAgQAAxkBAAIC6GbJ_lQM5wdANfD0y3cVzYzfeeoZAAJiKgAC3p-pUAJPQs4-zeiQNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate49, caption="""Could (do) and could have (done):""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate50")
async def upper_intermediate_50(call: CallbackQuery):
    upper_intermediate50 = "BAACAgQAAxkBAAIC6mbJ_l6GuF9Z1STLuM2OKVSRvCxEAAImRwACtXfQUJG8bq8VD-IMNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate50, caption="""Must and can't:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate51")
async def upper_intermediate_51(call: CallbackQuery):
    upper_intermediate51 = "BAACAgQAAxkBAAIC7GbJ_nCSr37LBVHT-tGTjLYu_GSjAALjRwACtXfQUKQehaWvrbrSNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate51, caption="""May and might:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate52")
async def upper_intermediate_52(call: CallbackQuery):
    upper_intermediate52 = "BAACAgQAAxkBAAIC7mbJ_oU62n2ck1qVtlR_mJdLdLx5AAJcSgACtXfQUNryu8qhvcY8NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate52, caption="""May and might 2:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate53")
async def upper_intermediate_53(call: CallbackQuery):
    upper_intermediate53 = "BAACAgQAAxkBAAIC8GbJ_pw7nqLNEhwDMPTC5wABsXU5HQACJkoAArV30FAC-n0x2qv6-DUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate53, caption="""Should 2:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate54")
async def upper_intermediate_54(call: CallbackQuery):
    upper_intermediate54 = "BAACAgIAAxkBAAIC8mbKD0RctTlqZkhY44X2XruEs_gTAAJzWQACMO5RSkgaNW1SkH-rNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate54, caption="""I'd better... / It's time...:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate55")
async def upper_intermediate_55(call: CallbackQuery):
    upper_intermediate55 = "BAACAgIAAxkBAAIC9GbKD4A8FfJkGKuqp_kn9YEQPxmyAAJZOQACMAWgSsMRmFjSPa2ZNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate55, caption="""Would:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate56")
async def upper_intermediate_56(call: CallbackQuery):
    upper_intermediate56 = "BAACAgIAAxkBAAIC9mbKEiJhGMLgp0NEUfJwPfZh3yaoAALGMQACL4vQSocNLssmM-aeNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate56, caption="""If I knew... I wish I knew...:""", reply_markup=back_5_6_btn)


@dp.callback_query_handler(text="upper_intermediate57")
async def upper_intermediate_57(call: CallbackQuery):
    upper_intermediate57 = "BAACAgIAAxkBAAIC-GbKEkJ9e_MUHrjXNuCQusbfqIOAAAKlJwACXJL4StERfOHH_9f4NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate57, caption="""Reported speech (He said that...):""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate58")
async def upper_intermediate_58(call: CallbackQuery):
    upper_intermediate58 = "BAACAgIAAxkBAAIC-mbKElbP_gQHWB5UbEP3IFakUCy2AAJvKwACggwYS0tWPoSglpi7NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate58, caption="""Verb + -ing (enjoy doing/ stop doing etc.):""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate59")
async def upper_intermediate_59(call: CallbackQuery):
    upper_intermediate59 = "BAACAgIAAxkBAAIC_GbKEnBeeaW1SivaBki-DgodHhvrAAIvNgACCAgpS1t6KDREyL9cNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate59, caption="""Verb+ to... ( decide to/ forget to.... etc.):""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate60")
async def upper_intermediate_60(call: CallbackQuery):
    upper_intermediate60 = "BAACAgIAAxkBAAIC_mbKEoTIhecRDW5lpzEeKAIa-IldAAJGMAACVqlBS4c4SCa5-0AkNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate60, caption="""Verb + -ing or to .... (remember, regret etc.):""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate61")
async def upper_intermediate_61(call: CallbackQuery):
    upper_intermediate61 = "BAACAgIAAxkBAAIDAAFmyhKdwjkahqhcObNhddz0pgOV4wACUjMAAtK3WUu6oAfk88T_PjUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate61, caption="""Verb + -ing or to ... 2 (try, need, help):""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate62")
async def upper_intermediate_62(call: CallbackQuery):
    upper_intermediate62 = "BAACAgIAAxkBAAIDAmbKEqkFa34MtkLAZ7BNg06N-tmMAAKWLwACjApwS-evRye1J49UNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate62, caption="""Prefer and would rather:""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate63")
async def upper_intermediate_63(call: CallbackQuery):
    upper_intermediate63 = "BAACAgIAAxkBAAIDWGbKKOXn5gROBea_RofpsnMQwiIQAAIWMQACeOLBSMZTI6EDNa3INQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate63, caption="""To..., for.... and so that...:""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate64")
async def upper_intermediate_64(call: CallbackQuery):
    upper_intermediate64 = "BAACAgIAAxkBAAIDWmbKKYnBn4Y-M58unHuUcpIlMb3wAAIqMQACEn4BSXtsHMS3vnknNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate64, caption="""Adjective + to...:""", reply_markup=back_5_7_btn)


@dp.callback_query_handler(text="upper_intermediate65")
async def upper_intermediate_65(call: CallbackQuery):
    upper_intermediate65 = "BAACAgIAAxkBAAIDXmbKKd-nlIDvDdw8WMsXH_UBV6KFAAIcLwACkTMRSagmoniXI43aNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate65, caption="""Countable and uncountable:""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate66")
async def upper_intermediate_66(call: CallbackQuery):
    upper_intermediate66 = "BAACAgIAAxkBAAIDY2bKKhFouSOO9nFCL5EjSjPLcwUZAAKAMgACpDchSTGefXkuSrOzNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate66, caption="""Countable nouns with a/an and some:""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate67")
async def upper_intermediate_67(call: CallbackQuery):
    upper_intermediate67 = "BAACAgIAAxkBAAIDZ2bKKqhtMH2ZZf--8ixNIcW50J6kAAIfMAACX0BJSROcTQLG_ANsNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate67, caption="""Singular and plural:""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate68")
async def upper_intermediate_68(call: CallbackQuery):
    upper_intermediate68 = "BAACAgIAAxkBAAIDaWbKKrtocFZpuHpFBdssvHRqYDoJAAImMQACo6pISXepdfQG8bHiNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate68, caption="""Noun+noun ( a bus driver/ a headache):""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate69")
async def upper_intermediate_69(call: CallbackQuery):
    upper_intermediate69 = "BAACAgIAAxkBAAIDbWbKKxYbvtKk1L6Lh4bblR2b-N9xAAIyYgACXaMoShHlf_XRuX9fNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate69, caption="""'s (your sister' name) and of ... (the name of the book):""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate70")
async def upper_intermediate_70(call: CallbackQuery):
    upper_intermediate70 = "BAACAgIAAxkBAAIDa2bKKuQXnKQwDS99awlsSTKGUvb4AAJ1NwAC8reASblzyEMYiLsBNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate70, caption="""Each and every:""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate71")
async def upper_intermediate_71(call: CallbackQuery):
    upper_intermediate71 = "BAACAgIAAxkBAAIDb2bKK0RBnAonOFXLe7Lqmre2hE-MAAKqNQACBH2ZSeDCOpvk1AUjNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate71, caption="""Relative clauses: whose/whom/where""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate72")
async def upper_intermediate_72(call: CallbackQuery):
    upper_intermediate72 = "BAACAgIAAxkBAAIDcWbKK132omvreyRtMGtiti4PFvcWAAJMNgACa_mxSYrQzOheioNINQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate72, caption="""Adjectives and Adverbs ( Quick/ Quickly ):""", reply_markup=back_5_8_btn)


@dp.callback_query_handler(text="upper_intermediate73")
async def upper_intermediate_73(call: CallbackQuery):
    upper_intermediate73 = "BAACAgIAAxkBAAIDc2bKK3pKWkrGgTIKHhng8mPU7bXsAAI6MgAC5XfJSV7T5QWuqc5iNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate73, caption="""Adjectives and Adverbs - 2 (Well, fast, late, hard/hardly):""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate74")
async def upper_intermediate_74(call: CallbackQuery):
    upper_intermediate74 = "BAACAgIAAxkBAAIDdWbKK5bD5tcGK8BDz_5MEt8Idz4iAAK2OQACnabhSQQ_erjGN31cNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate74, caption="""Enough and too:""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate75")
async def upper_intermediate_75(call: CallbackQuery):
    upper_intermediate75 = "BAACAgIAAxkBAAIDd2bKK_tTN0A-V-9hMI4Z0f6hKtY1AALvMgACCqUBSheksFzduLGqNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate75, caption="""Quite, pretty, rather and fairly:""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate76")
async def upper_intermediate_76(call: CallbackQuery):
    upper_intermediate76 = "BAACAgIAAxkBAAIDeWbKLC55RyI_3dqrs00cxe5j0mV6AALiWAACqXkpSno_ojYzdEDqNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate76, caption="""Comparative 1 (cheaper, more expensive etc.):""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate77")
async def upper_intermediate_77(call: CallbackQuery):
    upper_intermediate77 = "BAACAgIAAxkBAAIDe2bKLFqt3yjs8dR2r9mKK1tU6tWbAAL-ZQACjs8gShb8KdszeOlnNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate77, caption="""Comparative - 2 (much better/ any better etc.):""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate78")
async def upper_intermediate_78(call: CallbackQuery):
    upper_intermediate78 = "BAACAgIAAxkBAAIDfWbKLHz-SDyA_M5l8C7OixYah4dlAAJ0XQACE6goSs23xW5kzX99NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate78, caption="""Superlative (the longest/ the most enjoyable etc.):""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate79")
async def upper_intermediate_79(call: CallbackQuery):
    upper_intermediate79 = "BAACAgIAAxkBAAIDf2bKLLx-CR6bObPEAAGfuv2MvWkJAQACc2QAAhulIUqVCjyRQBruUDUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate79, caption="""Although, though, even, though, in spite of, despite:""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate80")
async def upper_intermediate_80(call: CallbackQuery):
    upper_intermediate80 = "BAACAgIAAxkBAAIDgWbKLNkbc8w_4kQmG2_eq9k8VZxvAAI3ZAACG6UhSru6kkKkkzSgNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate80, caption="""Even:""", reply_markup=back_5_9_btn)


@dp.callback_query_handler(text="upper_intermediate81")
async def upper_intermediate_81(call: CallbackQuery):
    upper_intermediate81 = "BAACAgIAAxkBAAIDg2bKLOq_yjZCPgABbJJa_TwS2o0uLAACfFkAAiQGKEo3-fZvOXYosDUE"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate81, caption="""Still, any, more, yet, already:""", reply_markup=back_5_10_btn)


@dp.callback_query_handler(text="upper_intermediate82")
async def upper_intermediate_82(call: CallbackQuery):
    upper_intermediate82 = "BAACAgIAAxkBAAIDhWbKLPXT9z6ZueRLe40pKQRq3COrAAJNZgACjs8gSv5jNZAw6HbbNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate82, caption="""Word order 1: verb + object; Place and time:""", reply_markup=back_5_10_btn)


@dp.callback_query_handler(text="upper_intermediate83")
async def upper_intermediate_83(call: CallbackQuery):
    upper_intermediate83 = "BAACAgIAAxkBAAIDh2bKLQYxHo23Zlip7qaczmQUUdZ-AAInWQACqXkpSrK4jC5QujzENQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate83, caption=""" As ( As I walked..../ As I was.... etc.):""", reply_markup=back_5_10_btn)


@dp.callback_query_handler(text="upper_intermediate84")
async def upper_intermediate_84(call: CallbackQuery):
    upper_intermediate84 = "BAACAgIAAxkBAAIDiWbKLRXefYYPNO9xJ5rBsGaDs03LAAJEWQACqXkpSohbC006f8MqNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate84, caption="""Like and as:""", reply_markup=back_5_10_btn)


@dp.callback_query_handler(text="upper_intermediate85")
async def upper_intermediate_85(call: CallbackQuery):
    upper_intermediate85 = "BAACAgIAAxkBAAIDi2bKLSLY_IERPBOOS4omS4B9OpA9AAIeWQACqXkpSlmo4XmNdlMQNQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate85, caption="""Like, as, if:""", reply_markup=back_5_10_btn)


@dp.callback_query_handler(text="upper_intermediate86")
async def upper_intermediate_86(call: CallbackQuery):
    upper_intermediate86 = "BAACAgIAAxkBAAIDjWbKLS-S39iGw-Y-UbCRg9-cys8gAAIPYgACXaMoSp3_q7-iM379NQQ"
    await call.message.delete()
    await call.message.answer_video(video=upper_intermediate86, caption="""At, on, in (time)""", reply_markup=back_5_10_btn)