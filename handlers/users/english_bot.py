from aiogram import types
from aiogram.types import Message, CallbackQuery
from loader import dp
from keyboards.default.default_keyboards import start_btn, ha_yoq_btn, telefon_btn
from keyboards.inline.inline_keyboards import beginner_btn, elementry_btn, pre_intermediate_btn, back4_btn, pre_intermediate2_btn, pre_intermediate3_btn, intermediate_btn, intermediate2_btn, intermediate3_btn, intermediate4_btn, upper_intermediate_btn, upper_intermediate_2_btn, upper_intermediate_3_btn, upper_intermediate_4_btn, upper_intermediate_5_btn, upper_intermediate_6_btn, upper_intermediate_7_btn, upper_intermediate_8_btn, upper_intermediate_9_btn, upper_intermediate_10_btn, upper_intermediate_11_btn, admin_bilan_boglanish_btn


@dp.message_handler(text="Admin bilan bog'lanish📲")
async def admin(msg: Message):
    await msg.answer("☎️Admin bilan bog'lanmoqchimisiz?", reply_markup=admin_bilan_boglanish_btn)


@dp.message_handler(text="Yo'q❌")
async def yoq_(msg: Message):
    await msg.answer("Qa'bul qilinmadi.", reply_markup=start_btn)


@dp.message_handler(text="Ha✅")
async def h_a(msg: Message):
    await msg.answer("Qa'bul qilindi.", reply_markup=start_btn)


@dp.callback_query_handler(text="yo'q")
async def yoq(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Admin bilan bo'g'lanish bekor qilindi.")


@dp.message_handler(text="A1 | Beginner📕")
async def beginner(msg: Message):
    await msg.answer("""Beginner levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Alifbo🔠

2-dars: To be verb🔠

3-dars: To be verb|Question forms🔠

4-dars: Present Continous Tense🔠

5-dars: Present Continuous Questions🔠

6-dars: Present Simple Tense🔠

7-dars: Present Simple Negative🔠

8-dars: Present Simple questions🔠""", reply_markup=beginner_btn)


@dp.message_handler(text="A2 | Elementry📗")
async def beginner(msg: Message):
    await msg.answer("""Elementry levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Present Simple and Present Continuous🔠

2-dars: I have got ... and I have ...🔠

3-dars: Past Simple(was/were)🔠

4-dars: Past Simple(positive)🔠

5-dars: Past Simple Negative and Questions🔠

6-dars: Past Continuous🔠

7-dars: Present Simple and Past Continuous🔠""", reply_markup=elementry_btn)


@dp.message_handler(text="A2-B1 | Pre-Intermediate📘")
async def beginner(msg: Message):
    await msg.answer("""Pre-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Present Perfect🔠

2-dars: Present Perfect 2🔠

3-dars: Present Perfect 3🔠

4-dars: Present Perfect🔠

5-dars: Since/For/Ago🔠

6-dars: Present Perfect and Past Simple🔠

7-dars: Passive voice🔠

8-dars: Passive voice 2🔠""", reply_markup=pre_intermediate_btn)


@dp.callback_query_handler(text="pre_intermediate2_")
async def pre_intermediate2_q(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: Present and Past tenses🔠

10-dars: Regular and Irregular verbes🔠

11-dars: Used to ...🔠

12-dars: What are you doing tommorrow?🔠

13-dars: I am going to🔠

14-dars: Future tenses🔠

15-dars: Future tenses 2🔠

16-dars: Modal verbs🔠""", reply_markup=pre_intermediate2_btn)


@dp.callback_query_handler(text="pre_intermediate3_")
async def pre_intermediate2_q(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""17-dars: Modal verbs 2🔠

18-dars: Modal verbes 3🔠

19-dars: Modal verbes 4🔠

20-dars: I have to ...🔠

21-dars: Would you like to ...🔠

22-dars: There is vs There are🔠

23-dars: There was vs There were🔠

24-dars: It ...🔠""", reply_markup=pre_intermediate3_btn)


@dp.message_handler(text="B1 | Intermediate📙")
async def beginner(msg: Message):
    await msg.answer("""Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: I'm vs I do🔠

2-dars: Question forms of all tenses🔠

3-dars: Too/either/neither do/So am I🔠

4-dars: Haven't/Don't/Isn't🔠

5-dars: Have you ... ?/ Do they ... ?🔠

6-dars: Who saw you? vs Who did you see?🔠

7-dars: Who say you vs Who did you see🔠""", reply_markup=intermediate_btn)


@dp.callback_query_handler(text="intermediate2_")
async def intermediate_2_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""8-dars: What is it like?🔠

9-dars: What? / Which? / How?🔠

10-dars: How does it take?🔠

11-dars: Do you know where ... ?🔠

12-dars: She said that🔠

13-dars: Work vs working🔠

14-dars: I want to do vs I enjoy doing🔠""", reply_markup=intermediate2_btn)


@dp.callback_query_handler(text="intermediate3_")
async def intermediate_3_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""15-dars: I told you to ...🔠

16-dars: I went to the shop to ...🔠

17-dars: Go to / Go on / Go for🔠

18-dars: Get a letter / Get a job🔠

19-dars: Do vs Make 🔠

20-dars: Have or Have got🔠

21-dars: Pronouns🔠""", reply_markup=intermediate3_btn)


@dp.callback_query_handler(text="intermediate4_")
async def intermediate_4_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""22-dars: Pronouns 2🔠

23-dars: Pronouns🔠

24-dars: Pronouns 2🔠

25-dars: -ning kelishik qo'shimchasi🔠

26-dars: A and an articles🔠

27-dars: Singular and Plural nouns🔠

28-dars: Countable and Uncountable nouns🔠""", reply_markup=intermediate4_btn)


@dp.message_handler(text="B2 | Upper-Intermediate📔")
async def beginner(msg: Message):
    await msg.answer("""Upper-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: A vs The Articles🔠

2-dars: The article🔠

3-dars: Go to work vs Go home🔠

4-dars: When NOT to use "the"🔠

5-dars: Names of places🔠

6-dars: This/That/Those/These🔠

7-dars: One vs Ones🔠

8-dars: Some vs Any🔠""", reply_markup=upper_intermediate_btn)


@dp.callback_query_handler(text="upper_intermediate2_")
async def upper_intermediate_2_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: No + any/No/None🔠

10-dars: Not+anybody vs Nobody🔠

11-dars: Somebody/Anything/Nowhere🔠

12-dars: Every vs All🔠

13-dars: All/Most/Some/Any🔠

14-dars: Both/Either/Neither🔠

15-dars: A lot/much/many🔠

16-dars: A little vs A few🔠""", reply_markup=upper_intermediate_2_btn)


@dp.callback_query_handler(text="upper_intermediate3_")
async def upper_intermediate_3_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""17-dars: Adjectives🔠

18-dars: Adverbs🔠

19-dars: Old vs older🔠

20-dars: Older/More expensive than ...🔠

21-dars: Not as ... as🔠

22-dars: The oldest/The most expensive🔠

23-dars: Enough🔠

24-dars: Too🔠""", reply_markup=upper_intermediate_3_btn)


@dp.callback_query_handler(text="upper_intermediate4_")
async def upper_intermediate_4_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""25-dars: Word order🔠

26-dars: Word order 2🔠

27-dars: Still vs Yet🔠

28-dars: Give me .../ Give it to🔠

29-dars: At/On/In🔠

30-dars: From... to, Until, Since, For🔠

31-dars: Before, After, During, While🔠

32-dars: In/At (Places)🔠""", reply_markup=upper_intermediate_4_btn)


@dp.callback_query_handler(text="upper_intermediate5_")
async def upper_intermediate_5_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""33-dars: In/At/On (places 2)🔠

34-dars: In/At/On (places 3)🔠

35-dars: On/Under/Behind (prepositions)🔠

36-dars: Up/Over/Through (prepositions)🔠

37-dars: At/By/With/Without/About (prepositions)🔠

38-dars: Afraid of... / On holiday (word + prpositions)🔠

39-dars: Look at / Listen to (verb + prepostions)🔠

40-dars: Go in / Fall off / Run away (phrasal verb 1)🔠""", reply_markup=upper_intermediate_5_btn)


@dp.callback_query_handler(text="upper_intermediate6_")
async def upper_intermediate_6_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""41-dars: Put on your shoes / Put your shoes on  (phrasal verb 1)🔠

42-dars: And / But / Or / So / Because🔠

43-dars: When?🔠

44-dars: If we go ... If you see ...🔠

45-dars:  If I had... If we went...🔠

45-dars: A person who ...  a thing that/which (relative clauses 1)🔠

47-dars: The people we met the hotel you stayed at🔠

48-dars: Can\could and (be) able to🔠""", reply_markup=upper_intermediate_6_btn)


@dp.callback_query_handler(text="upper_intermediate7_")
async def upper_intermediate_7_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""49-dars: Could (do) and could have (done)🔠
    
50-dars: Must and can't🔠

51-dars: May and might🔠

52-dars: May and might 2🔠

53-dars: Should 2🔠

54-dars: I'd better... / It's time...🔠 

55-dars: Would🔠

56-dars: If I knew... I wish I knew...🔠""", reply_markup=upper_intermediate_7_btn)


@dp.callback_query_handler(text="upper_intermediate8_")
async def upper_intermediate_8_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""57-dars: Reported speech (He said that...)🔠
    
58-dars: Verb + -ing (enjoy doing/ stop doing etc.)🔠
    
59-dars: Verb+ to... ( decide to/ forget to.... etc.)🔠

60-dars: Verb + -ing or to .... (remember, regret etc.)🔠

61-dars: Verb + -ing or to ... 2 (try, need, help)🔠

62-dars: Prefer and would rather🔠

63-dars: To..., for.... and so that...🔠

64-dars: Adjective + to...🔠""", reply_markup=upper_intermediate_8_btn)


@dp.callback_query_handler(text="upper_intermediate9_")
async def upper_intermediate9_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""65-dars: Countable and uncountable🔠
    
66-dars: Countable nouns with a/an and some🔠
    
67-dars: Singular and plural🔠

68-dars: Noun+noun ( a bus driver/ a headache)🔠

69-dars: 's (your sister' name) and of ... (the name of the book)🔠

70-dars: Each and every🔠

71-dars: Relative clauses: whose/whom/where🔠

72-dars: Adjectives and Adverbs ( Quick/ Quickly )🔠""", reply_markup=upper_intermediate_9_btn)


@dp.callback_query_handler(text="upper_intermediate10_")
async def upper_intermediate_10_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""73-dars: Adjectives and Adverbs - 2 (Well, fast, late, hard/hardly)🔠
    
74-dars: Enough and too🔠
    
75-dars: Quite, pretty, rather and fairly🔠

76-dars: Comparative 1 (cheaper, more expensive etc.)🔠

77-dars: Comparative - 2 (much better/ any better etc.)🔠 

78-dars: Superlative (the longest/ the most enjoyable etc.)🔠 

79-dars: Although, though, even, though, in spite of, despite🔠

80-dars: Even🔠""", reply_markup=upper_intermediate_10_btn)


@dp.callback_query_handler(text="upper_intermediate11_")
async def upper_intermediate_11_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""81-dars: Still, any, more, yet, already🔠
    
82-dars: Word order 1: verb + object; Place and time🔠
    
83-dars: As ( As I walked..../ As I was.... etc.)🔠

84-dars: Like and as🔠

85-dars: Like, as, if🔠

86-dars: At, on, in (time)🔠""", reply_markup=upper_intermediate_11_btn)


@dp.callback_query_handler(text="bback")
async def back1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Beginner levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Alifbo🔠

2-dars: To be verb🔠

3-dars: To be verb|Question forms🔠

4-dars: Present Continous Tense🔠

5-dars: Present Continuous Questions🔠

6-dars: Present Simple Tense🔠

7-dars: Present Simple Negative🔠

8-dars: Present Simple questions🔠""", reply_markup=beginner_btn)


@dp.callback_query_handler(text="eback")
async def back2(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Elementry levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Present Simple and Present Continuous🔠

2-dars: I have got ... and I have ...🔠

3-dars: Past Simple(was/were)🔠

4-dars: Past Simple(positive)🔠

5-dars: Past Simple Negative and Questions🔠

6-dars: Past Continuous🔠

7-dars: Present Simple and Past Continuous🔠""", reply_markup=elementry_btn)


@dp.callback_query_handler(text="pback")
async def back3(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Pre-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Present Perfect🔠

2-dars: Present Perfect 2🔠

3-dars: Present Perfect 3🔠

4-dars: Present Perfect🔠

5-dars: Since/For/Ago🔠

6-dars: Present Perfect and Past Simple🔠

7-dars: Passive voice🔠

8-dars: Passive voice 2🔠""", reply_markup=pre_intermediate_btn)


@dp.callback_query_handler(text="p2back")
async def p_2back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Pre-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: Present Perfect🔠

2-dars: Present Perfect 2🔠

3-dars: Present Perfect 3🔠

4-dars: Present Perfect🔠

5-dars: Since/For/Ago🔠

6-dars: Present Perfect and Past Simple🔠

7-dars: Passive voice🔠

8-dars: Passive voice 2🔠""", reply_markup=pre_intermediate_btn)


@dp.callback_query_handler(text="p_2_back")
async def p_2_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: Present and Past tenses🔠

10-dars: Regular and Irregular verbes🔠

11-dars: Used to ...🔠

12-dars: What are you doing tommorrow?🔠

13-dars: I am going to🔠

14-dars: Future tenses🔠

15-dars: Future tenses 2🔠

16-dars: Modal verbs🔠""", reply_markup=pre_intermediate2_btn)


@dp.callback_query_handler(text="p3back")
async def p_3back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: Present and Past tenses🔠

10-dars: Regular and Irregular verbes🔠

11-dars: Used to ...🔠

12-dars: What are you doing tommorrow?🔠

13-dars: I am going to🔠

14-dars: Future tenses🔠

15-dars: Future tenses 2🔠

16-dars: Modal verbs🔠""", reply_markup=pre_intermediate2_btn)


@dp.callback_query_handler(text="p_3_back")
async def p_3_2back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""17-dars: Modal verbs 2🔠

18-dars: Modal verbes 3🔠

19-dars: Modal verbes 4🔠

20-dars: I have to ...🔠

21-dars: Would you like to ...🔠

22-dars: There is vs There are🔠

23-dars: There was vs There were🔠

24-dars: It ...🔠""", reply_markup=pre_intermediate3_btn)


@dp.callback_query_handler(text="iback")
async def back4(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: I'm vs I do🔠

2-dars: Question forms of all tenses🔠

3-dars: Too/either/neither do/So am I🔠

4-dars: Haven't/Don't/Isn't🔠

5-dars: Have you ... ?/ Do they ... ?🔠

6-dars: Who saw you? vs Who did you see?🔠

7-dars: Who say you vs Who did you see🔠""", reply_markup=intermediate_btn)


@dp.callback_query_handler(text="i2back")
async def i_2back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: I'm vs I do🔠

2-dars: Question forms of all tenses🔠

3-dars: Too/either/neither do/So am I🔠

4-dars: Haven't/Don't/Isn't🔠

5-dars: Have you ... ?/ Do they ... ?🔠

6-dars: Who saw you? vs Who did you see?🔠

7-dars: Who say you vs Who did you see🔠""", reply_markup=intermediate_btn)


@dp.callback_query_handler(text="i_2back")
async def p_2_back_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""8-dars: What is it like?🔠

9-dars: What? / Which? / How?🔠

10-dars: How does it take?🔠

11-dars: Do you know where ... ?🔠

12-dars: She said that🔠

13-dars: Work vs working🔠

14-dars: I want to do vs I enjoy doing🔠""", reply_markup=intermediate2_btn)


@dp.callback_query_handler(text="i3back")
async def i_3back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""8-dars: What is it like?🔠

9-dars: What? / Which? / How?🔠

10-dars: How does it take?🔠

11-dars: Do you know where ... ?🔠

12-dars: She said that🔠

13-dars: Work vs working🔠

14-dars: I want to do vs I enjoy doing🔠""", reply_markup=intermediate2_btn)


@dp.callback_query_handler(text="i_3back")
async def p_3_back_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""15-dars: I told you to ...🔠

16-dars: I went to the shop to ...🔠

17-dars: Go to / Go on / Go for🔠

18-dars: Get a letter / Get a job🔠

19-dars: Do vs Make 🔠

20-dars: Have or Have got🔠

21-dars: Pronouns🔠""", reply_markup=intermediate3_btn)


@dp.callback_query_handler(text="i4back")
async def i_4back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""15-dars: I told you to ...🔠

16-dars: I went to the shop to ...🔠

17-dars: Go to / Go on / Go for🔠

18-dars: Get a letter / Get a job🔠

19-dars: Do vs Make 🔠

20-dars: Have or Have got🔠

21-dars: Pronouns🔠""", reply_markup=intermediate3_btn)


@dp.callback_query_handler(text="i_4back")
async def i_4_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""22-dars: Pronouns 2🔠

23-dars: Pronouns🔠

24-dars: Pronouns 2🔠

25-dars: -ning kelishik qo'shimchasi🔠

26-dars: A and an articles🔠

27-dars: Singular and Plural nouns🔠

28-dars: Countable and Uncountable nouns🔠""", reply_markup=intermediate4_btn)


@dp.callback_query_handler(text="uback")
async def back5(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Upper-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: A vs The Articles🔠

2-dars: The article🔠

3-dars: Go to work vs Go home🔠

4-dars: When NOT to use "the"🔠

5-dars: Names of places🔠

6-dars: This/That/Those/These🔠

7-dars: One vs Ones🔠

8-dars: Some vs Any🔠""", reply_markup=upper_intermediate_btn)


@dp.callback_query_handler(text="u2back")
async def u2_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""Upper-Intermediate levelining video darslar:
Mavzuni tanlang 👇:

1-dars: A vs The Articles🔠

2-dars: The article🔠

3-dars: Go to work vs Go home🔠

4-dars: When NOT to use "the"🔠

5-dars: Names of places🔠

6-dars: This/That/Those/These🔠

7-dars: One vs Ones🔠

8-dars: Some vs Any🔠""", reply_markup=upper_intermediate_btn)


@dp.callback_query_handler(text="u3back")
async def u3_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: No + any/No/None🔠

10-dars: Not+anybody vs Nobody🔠

11-dars: Somebody/Anything/Nowhere🔠

12-dars: Every vs All🔠

13-dars: All/Most/Some/Any🔠

14-dars: Both/Either/Neither🔠

15-dars: A lot/much/many🔠

16-dars: A little vs A few🔠""", reply_markup=upper_intermediate_2_btn)


@dp.callback_query_handler(text="u_2back")
async def u_2_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""9-dars: No + any/No/None🔠

10-dars: Not+anybody vs Nobody🔠

11-dars: Somebody/Anything/Nowhere🔠

12-dars: Every vs All🔠

13-dars: All/Most/Some/Any🔠

14-dars: Both/Either/Neither🔠

15-dars: A lot/much/many🔠

16-dars: A little vs A few🔠""", reply_markup=upper_intermediate_2_btn)


@dp.callback_query_handler(text="u4back")
async def u4_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""17-dars: Adjectives🔠

18-dars: Adverbs🔠

19-dars: Old vs older🔠

20-dars: Older/More expensive than ...🔠

21-dars: Not as ... as🔠

22-dars: The oldest/The most expensive🔠

23-dars: Enough🔠

24-dars: Too🔠""", reply_markup=upper_intermediate_3_btn)


@dp.callback_query_handler(text="u_3back")
async def u_3_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""17-dars: Adjectives🔠

18-dars: Adverbs🔠

19-dars: Old vs older🔠

20-dars: Older/More expensive than ...🔠

21-dars: Not as ... as🔠

22-dars: The oldest/The most expensive🔠

23-dars: Enough🔠

24-dars: Too🔠""", reply_markup=upper_intermediate_3_btn)


@dp.callback_query_handler(text="u5back")
async def u5_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""25-dars: Word order🔠

26-dars: Word order 2🔠

27-dars: Still vs Yet🔠

28-dars: Give me .../ Give it to🔠

29-dars: At/On/In🔠

30-dars: From... to, Until, Since, For🔠

31-dars: Before, After, During, While🔠

32-dars: In/At (Places)🔠""", reply_markup=upper_intermediate_4_btn)


@dp.callback_query_handler(text="u_4back")
async def u_4_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""25-dars: Word order🔠

26-dars: Word order 2🔠

27-dars: Still vs Yet🔠

28-dars: Give me .../ Give it to🔠

29-dars: At/On/In🔠

30-dars: From... to, Until, Since, For🔠

31-dars: Before, After, During, While🔠

32-dars: In/At (Places)🔠""", reply_markup=upper_intermediate_4_btn)


@dp.callback_query_handler(text="u6back")
async def u6_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""33-dars: In/At/On (places 2)🔠

34-dars: In/At/On (places 3)🔠

35-dars: On/Under/Behind (prepositions)🔠

36-dars: Up/Over/Through (prepositions)🔠

37-dars: At/By/With/Without/About (prepositions)🔠

38-dars: Afraid of... / On holiday (word + prpositions)🔠

39-dars: Look at / Listen to (verb + prepostions)🔠

40-dars: Go in / Fall off / Run away (phrasal verb 1)🔠""", reply_markup=upper_intermediate_5_btn)


@dp.callback_query_handler(text="u_5back")
async def u_5_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""33-dars: In/At/On (places 2)🔠

34-dars: In/At/On (places 3)🔠

35-dars: On/Under/Behind (prepositions)🔠

36-dars: Up/Over/Through (prepositions)🔠

37-dars: At/By/With/Without/About (prepositions)🔠

38-dars: Afraid of... / On holiday (word + prpositions)🔠

39-dars: Look at / Listen to (verb + prepostions)🔠

40-dars: Go in / Fall off / Run away (phrasal verb 1)🔠""", reply_markup=upper_intermediate_5_btn)


@dp.callback_query_handler(text="u7back")
async def u7_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""41-dars: Put on your shoes / Put your shoes on  (phrasal verb 1)🔠

42-dars: And / But / Or / So / Because🔠

43-dars: When?🔠

44-dars: If we go ... If you see ...🔠

45-dars:  If I had... If we went...🔠

45-dars: A person who ...  a thing that/which (relative clauses 1)🔠

47-dars: The people we met the hotel you stayed at🔠

48-dars: Can\could and (be) able to🔠""", reply_markup=upper_intermediate_6_btn)


@dp.callback_query_handler(text="u_6back")
async def u_6_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""41-dars: Put on your shoes / Put your shoes on  (phrasal verb 1)🔠

42-dars: And / But / Or / So / Because🔠

43-dars: When?🔠

44-dars: If we go ... If you see ...🔠

45-dars:  If I had... If we went...🔠

45-dars: A person who ...  a thing that/which (relative clauses 1)🔠

47-dars: The people we met the hotel you stayed at🔠

48-dars: Can\could and (be) able to🔠""", reply_markup=upper_intermediate_6_btn)


@dp.callback_query_handler(text="u8back")
async def u8_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""49-dars: Could (do) and could have (done)🔠
    
50-dars: Must and can't🔠

51-dars: May and might🔠

52-dars: May and might 2🔠

53-dars: Should 2🔠

54-dars:  I'd better... / It's time...🔠 

55-dars: Would🔠

56-dars: If I knew... I wish I knew...🔠""", reply_markup=upper_intermediate_7_btn)


@dp.callback_query_handler(text="u_7back")
async def u_7_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""49-dars: Could (do) and could have (done)🔠
    
50-dars: Must and can't🔠

51-dars: May and might🔠

52-dars: May and might 2🔠

53-dars: Should 2🔠

54-dars:  I'd better... / It's time...🔠 

55-dars: Would🔠

56-dars: If I knew... I wish I knew...🔠""", reply_markup=upper_intermediate_7_btn)


@dp.callback_query_handler(text="u9back")
async def u9_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""57-dars: Reported speech (He said that...)🔠
    
58-dars: Verb + -ing (enjoy doing/ stop doing etc.)🔠
    
59-dars: Verb+ to... ( decide to/ forget to.... etc.)🔠

60-dars: Verb + -ing or to .... (remember, regret etc.)🔠

61-dars: Verb + -ing or to ... 2 (try, need, help)🔠

62-dars: Prefer and would rather🔠

63-dars: To..., for.... and so that...🔠

64-dars: Adjective + to...🔠""", reply_markup=upper_intermediate_8_btn)


@dp.callback_query_handler(text="u_8back")
async def u_8_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""57-dars: Reported speech (He said that...)🔠
    
58-dars: Verb + -ing (enjoy doing/ stop doing etc.)🔠
    
59-dars: Verb+ to... ( decide to/ forget to.... etc.)🔠

60-dars: Verb + -ing or to .... (remember, regret etc.)🔠

61-dars: Verb + -ing or to ... 2 (try, need, help)🔠

62-dars: Prefer and would rather🔠

63-dars: To..., for.... and so that...🔠

64-dars: Adjective + to...🔠""", reply_markup=upper_intermediate_8_btn)


@dp.callback_query_handler(text="u10back")
async def u10_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""65-dars: Countable and uncountable🔠
    
66-dars: Countable nouns with a/an and some🔠
    
67-dars: Singular and plural🔠

68-dars: Noun+noun ( a bus driver/ a headache)🔠

69-dars: 's (your sister' name) and of ... (the name of the book)🔠

70-dars: Each and every🔠

71-dars: Relative clauses: whose/whom/where🔠

72-dars: Adjectives and Adverbs ( Quick/ Quickly )🔠""", reply_markup=upper_intermediate_9_btn)


@dp.callback_query_handler(text="u_9back")
async def u_9_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""65-dars: Countable and uncountable🔠
    
66-dars: Countable nouns with a/an and some🔠
    
67-dars: Singular and plural🔠

68-dars: Noun+noun ( a bus driver/ a headache)🔠

69-dars: 's (your sister' name) and of ... (the name of the book)🔠

70-dars: Each and every🔠

71-dars: Relative clauses: whose/whom/where🔠

72-dars: Adjectives and Adverbs ( Quick/ Quickly )🔠""", reply_markup=upper_intermediate_9_btn)


@dp.callback_query_handler(text="u11back")
async def u11_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""73-dars: Adjectives and Adverbs - 2 (Well, fast, late, hard/hardly)🔠
    
74-dars: Enough and too🔠
    
75-dars: Quite, pretty, rather and fairly🔠

76-dars: Comparative 1 (cheaper, more expensive etc.)🔠

77-dars: Comparative - 2 (much better/ any better etc.)🔠 

78-dars: Superlative (the longest/ the most enjoyable etc.)🔠 

79-dars: Although, though, even, though, in spite of, despite🔠

80-dars: Even🔠""", reply_markup=upper_intermediate_10_btn)


@dp.callback_query_handler(text="u_10back")
async def u_10_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""73-dars: Adjectives and Adverbs - 2 (Well, fast, late, hard/hardly)🔠
    
74-dars: Enough and too🔠
    
75-dars: Quite, pretty, rather and fairly🔠

76-dars: Comparative 1 (cheaper, more expensive etc.)🔠

77-dars: Comparative - 2 (much better/ any better etc.)🔠 

78-dars: Superlative (the longest/ the most enjoyable etc.)🔠 

79-dars: Although, though, even, though, in spite of, despite🔠

80-dars: Even🔠""", reply_markup=upper_intermediate_10_btn)


@dp.callback_query_handler(text="u11back")
async def u11_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""81-dars: Still, any, more, yet, already🔠
    
82-dars: Word order 1: verb + object; Place and time🔠
    
83-dars: As ( As I walked..../ As I was.... etc.)🔠

84-dars: Like and as🔠

85-dars: Like, as, if🔠

86-dars: At, on, in (time)🔠""", reply_markup=upper_intermediate_11_btn)