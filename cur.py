from aiogram import Dispatcher,types,executor,Bot
import requests,logging
url= 'https://v6.exchangerate-api.com/v6/6a99f146537c10ce0eba4626/pair/USD/UZS'
bottoken='2145205223:AAEqFoDea3ps4el1DkWpy3iycUc4znY7U6A'
response = requests.get(url)
data = response.json()


logging.basicConfig(level=logging.INFO)
bot=Bot(token=bottoken)
dp=Dispatcher(bot)

# Where USD is the base currency you want to use
@dp.message_handler(commands='start')
async def sendwelcome(message: types.Message):
    await message.answer('Assalomu aleykum men Sevaraning uchinchi raqamli botiman. Kurs qiymatini bilish uchun /kurs buyurugini bering. Yordam ouchun /yordam ustiga bosing')
@dp.message_handler(commands='yordam')
async def yordam(message:types.Message):
    await message.answer('Valyuta kursni bilish uchun /kurs ni ustiga bosing. Yordam olish uchun @sevaraxon2002 ga murojaat qiling')
# Making our request
@dp.message_handler(commands='kurs')
async def kursimiz(message: types.Message):
    kurs=str(data['conversion_rate'])
    oxrgisana=str(data['time_last_update_utc'])
    await message.answer(oxrgisana+' sana xisobi bilan 1$ = '+kurs+' somga')

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)