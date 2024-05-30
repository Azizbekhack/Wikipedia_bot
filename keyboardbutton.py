from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Computers"),KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"),KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")],
        [KeyboardButton(text="Orqaga")]
        
        

    ],
    resize_keyboard=True,
    input_field_placeholder="Choise button..."
)

computers = [
    "Mackbook",
    "Lenovo",
    "HP",
    "ASUS",
    "Victus",
    "ACER",
    "Samsung"
]

computers_info = {
    "Mackbook":{"photo":"https://univershop.uz/wp-content/uploads/2023/10/3-2.jpg","price":1200,"color":"Black"},
    "Lenovo":{"photo":"https://interbrands.uz/image/cache/catalog/HP/qc2r1m046oujnh9zj1wacjbkwnuu1n9a-1000x600.jpg","price":500,"color":"Blue"},
    "HP":{"photo":"https://assets.asaxiy.uz/product/items/desktop/e2ec8d2c9161c0120c59bef9ec4861602023031017010062176AAT7WGJnZ9.jpg.webp","price":850,"color":"Green"},
    "ASUS":{"photo":"https://m.media-amazon.com/images/I/71ehzrGUO7L._AC_SL1500_.jpg","price":750,"color":"Grey"},
    "Victus":{"photo":"https://notebookoff.uz/upload/resize_cache/iblock/a87/1200_1200_140cd750bba9870f18aada2478b24840a/oqyvkn2a47v1rbmerif5qikh6ef0odgn.jpg","price":800,"color":"Black"},
    "ACER":{"photo":"https://api.idea.uz/storage/products/March2023/q6YKRepfO9GQFDhii73y.png","price":700,"color":"Blue"},
    "Samsung":{"photo":"https://m.media-amazon.com/images/I/61oTh3Oun5L._AC_SL1500_.jpg","price":600,"color":"Red"},

}

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.adjust(2,repeat=True)
computer_button = computer_button.as_markup(resize_keyboard=True,input_field_placeholder="Choise computer...")


from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Computers"),KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"),KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")],
        [KeyboardButton(text="Orqaga")]
        
        

    ],
    resize_keyboard=True,
    input_field_placeholder="Choise button..."
)

phones = [
    "Iphone",
    "Redmi",
    "Sony",
    "Nokia",
    "Huawei",
    "Oppo",
    "Samsung"
]     


phones_info = {
    "Iphone":{"photo":"https://openshop.uz/public/storage/uploads/products/photos/202210/LAeHdDTNTM9Ao4rMLczeZGQMJRrcvdrkNPtEebcn.jpg","price":1200,"color":"Black"},
    "Redmi":{"photo":"https://btech.com/media/catalog/product/cache/22b1bed05f04d71c4a848d770186c3c4/4/0/4096061b786611ccfb7e9d363309ac442dabfec0bbcc50e899e6d3915b92e95f.jpeg","price":500,"color":"Blue"},
    "Sony":{"photo":"https://mma.prnewswire.com/media/2074315/Sony_X1V_khakiGreen.jpg","price":850,"color":"Green"},
    "Nokia":{"photo":"https://www.clove.co.uk/cdn/shop/files/nokia-g42-grey-front-back_5000x.jpg?v=1688056081","price":750,"color":"Grey"},
    "Huawei":{"photo":"https://consumer.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/p60-pro/images/hero/huawei-p60-pro-kv@2x.webp","price":800,"color":"Black"},
    "Oppo":{"photo":"https://api.idea.uz/storage/products/March2023/q6YKRepfO9GQFDhii73y.png","price":700,"color":"Blue"},
    "Samsung":{"photo":"https://m.media-amazon.com/images/I/61oTh3Oun5L._AC_SL1500_.jpg","price":600,"color":"Red"},

}

phones_button = ReplyKeyboardBuilder()

for phone in phones:
    phones_button.add(KeyboardButton(text=phone))

phones_button.adjust(2,repeat=True)
phones_button = phones_button.as_markup(resize_keyboard=True,input_field_placeholder="Choise phones...")