import mysql.connector
from datetime import datetime
import random

# Sample JSON data
# data = {
#   "results": [
#     {
#       "id": 1279,
#       "name": "The “Traditional Water Puppet Show”",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/03/21/08/2aff26681043246ebef537f075e2f861.png",
#       "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2022/06/16/3E9E3B.jpg",
#       "day": "2024-07-04T11:30:00Z",
#       "price": 300000,
#       "deeplink": "https://ticketbox.vn/chuong-trinh-mua-roi-nuoc-co-truyen-eng-84203",
#       "isNewBookingFlow": True,
#       "originalId": 84203,
#       "url": "chuong-trinh-mua-roi-nuoc-co-truyen-eng",
#       "badge": None
#     },
#     {
#       "id": 22702,
#       "name": "[BẾN THÀNH] Đêm nhạc Quang Dũng",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/59/82/57/f23e2c79d382700c8d1675feda151e7d.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/1e561f3085ce55623665db27cb3671ed.jpg",
#       "day": "2024-07-05T13:00:00Z",
#       "price": 500000,
#       "deeplink": "https://ticketbox.vn/ben-thanh-dem-nhac-quang-dung-22702",
#       "isNewBookingFlow": True,
#       "originalId": 22702,
#       "url": "ben-thanh-dem-nhac-quang-dung",
#       "badge": None
#     },
#     {
#       "id": 22402,
#       "name": "[Hà Nội] Những Thành Phố Mơ Màng Summer Tour 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/a0/37/5e/2db1319230e01ee3e519dbd1a34c6fcf.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/ea/6f/9c/0818985a6360ff4711e4a469f5ca5679.jpg",
#       "day": "2024-07-06T08:00:00Z",
#       "price": 389000,
#       "deeplink": "https://ticketbox.vn/ntpmm-ha-noi-22402",
#       "isNewBookingFlow": True,
#       "originalId": 22402,
#       "url": "ntpmm-ha-noi",
#       "badge": None
#     },
#     {
#       "id": 22631,
#       "name": "LULULOLA SHOW ƯNG HOÀNG PHÚC - NGUYỄN KIỀU OANH | NẾU TA CÒN YÊU NHAU",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/83/9b/e7/d87f0b648d52d24bf4ba4509c1c3f957.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/3fae41f9463aeb534cbcc2db6fb5fb28.jpg",
#       "day": "2024-07-06T10:30:00Z",
#       "price": 400000,
#       "deeplink": "https://ticketbox.vn/lululola-show-ung-hoang-phuc-nguyen-kieu-oanh-22631",
#       "isNewBookingFlow": True,
#       "originalId": 22631,
#       "url": "lululola-show-ung-hoang-phuc-nguyen-kieu-oanh",
#       "badge": None
#     },
#     {
#       "id": 22633,
#       "name": "MINI SHOW 06.07 TRƯƠNG THẢO NHI | SÂN KHẤU HỒ MÂY SHOW ",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/94/91/ed/498fbfe1c94828f08af4c888e2a25a8e.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/16/da/9c/02fb0a5dbee21d64c01cf93788b4ddee.png",
#       "day": "2024-07-06T11:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/mini-show-0607-truong-thao-nhi-san-khau-ho-may-show-22633",
#       "isNewBookingFlow": True,
#       "originalId": 22633,
#       "url": "mini-show-0607-truong-thao-nhi-san-khau-ho-may-show",
#       "badge": None
#     },
#     {
#       "id": 22683,
#       "name": "SAY HI THÁNG 7 CÙNG VAN PHUC WATER SHOW",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/bb/73/32/e3018dbae9ad106cd87b5698b2d16b21.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/66/9d/a1/668100f8fcd34c304d03737f6c2017bf.png",
#       "day": "2024-07-06T12:30:00Z",
#       "price": 50000,
#       "deeplink": "https://ticketbox.vn/say-hi-thang-7-cung-van-phuc-water-show-22683",
#       "isNewBookingFlow": True,
#       "originalId": 22683,
#       "url": "say-hi-thang-7-cung-van-phuc-water-show",
#       "badge": None
#     },
#     {
#       "id": 22671,
#       "name": "LULULOLA SHOW HOÀNG HẢI & THÙY CHI | NHẮN GIÓ MÂY RẰNG ANH YÊU EM",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/65/82/1e/23f76562706705c61e292b609df38ea1.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/cf347f3f30b63db7fff80eb372b5ad21.jpg",
#       "day": "2024-07-07T10:30:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/lululola-show-hoang-hai-thuy-chi-22671",
#       "isNewBookingFlow": True,
#       "originalId": 22671,
#       "url": "lululola-show-hoang-hai-thuy-chi",
#       "badge": None
#     },
#     {
#       "id": 22703,
#       "name": "[BẾN THÀNH] Đêm nhạc Lê Hiếu - Lâm Bảo Ngọc",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/2a/a4/da/b2b855dff68707d70acbaddd818ab613.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/fdb2f125f2001f68b1dca67656f3803b.jpg",
#       "day": "2024-07-10T13:00:00Z",
#       "price": 150000,
#       "deeplink": "https://ticketbox.vn/ben-thanh-dem-nhac-le-hieu-lam-bao-ngoc-22703",
#       "isNewBookingFlow": True,
#       "originalId": 22703,
#       "url": "ben-thanh-dem-nhac-le-hieu-lam-bao-ngoc",
#       "badge": None
#     },
#     {
#       "id": 22705,
#       "name": "[BẾN THÀNH] Đêm nhạc Hoàng Hải - Myra Trần",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/1a/cf/0a/dd89be01b53f00f260e91370a58fcc86.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/65b79e62874572954172a8e3ff894be5.jpg",
#       "day": "2024-07-11T13:00:00Z",
#       "price": 500000,
#       "deeplink": "https://ticketbox.vn/ben-thanh-dem-nhac-hoang-hai-myra-tran-22705",
#       "isNewBookingFlow": True,
#       "originalId": 22705,
#       "url": "ben-thanh-dem-nhac-hoang-hai-myra-tran",
#       "badge": None
#     },
#     {
#       "id": 22656,
#       "name": "[HẢI PHÒNG] LÊ HIẾU & VICKY NHUNG",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/4c/d7/fb/96ea174734ad3f98c1a51a2642885f63.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/9d/64/68/b8b6cf10d6deb1903d33e6efa970e51e.jpg",
#       "day": "2024-07-12T13:00:00Z",
#       "price": 400000,
#       "deeplink": "https://ticketbox.vn/hai-phong-le-hieu-vicky-nhung-22656",
#       "isNewBookingFlow": True,
#       "originalId": 22656,
#       "url": "hai-phong-le-hieu-vicky-nhung",
#       "badge": None
#     },
#     {
#       "id": 22600,
#       "name": "LULULOLA SHOW LÂN NHÃ KM BÙI LAN HƯƠNG",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/ff/c1/fe/5c11b48e9101d920e6a6a8bff33b712c.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/2dbb92411776036374c6f8e3f0c9d14c.jpg",
#       "day": "2024-07-13T10:30:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/lan-nha-bui-lan-huong-22600",
#       "isNewBookingFlow": True,
#       "originalId": 22600,
#       "url": "lan-nha-bui-lan-huong",
#       "badge": None
#     },
#     {
#       "id": 22204,
#       "name": "[HCM] TRUNG QUÂN  1689 - More than 1589",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/bb/e2/49/34560b519e0293e77d1b16bbaaefcf1c.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/ec47923339d2a1a6a4d060d1f4caaf18.jpg",
#       "day": "2024-07-13T12:00:00Z",
#       "price": 1000000,
#       "deeplink": "https://ticketbox.vn/hcm-trung-quan-1689-more-than-1589-89919-89919",
#       "isNewBookingFlow": True,
#       "originalId": 89919,
#       "url": "hcm-trung-quan-1689-more-than-1589-89919",
#       "badge": None
#     },
#     {
#       "id": 22670,
#       "name": "LULULOLA SHOW HOÀNG DŨNG KM LÂM PHÚC & MR BOTT BAND | ĐÔI LỜI TÌNH CA",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/b1/08/4f/15a974b605c705c9890cb9e3ca4a4b74.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/7591d680da64b93638461831541034d7.jpg",
#       "day": "2024-07-19T10:30:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/lululola-show-hoang-dung-km-lam-phuc-mr-bott-band-22670",
#       "isNewBookingFlow": True,
#       "originalId": 22670,
#       "url": "lululola-show-hoang-dung-km-lam-phuc-mr-bott-band",
#       "badge": None
#     },
#     {
#       "id": 22706,
#       "name": "[BẾN THÀNH] Đêm nhạc Thuỳ Dung - KM: Nguyễn Đình Tuấn Nghĩa",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/45/8a/ca/d2e4a4844120e3e9075098be0307efa3.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/b45f14cab4c44cbd17933ae0de399691.jpg",
#       "day": "2024-07-19T13:00:00Z",
#       "price": 300000,
#       "deeplink": "https://ticketbox.vn/ben-thanh-dem-nhac-thuy-dung-km-nguyen-dinh-tuan-nghia-22706",
#       "isNewBookingFlow": True,
#       "originalId": 22706,
#       "url": "ben-thanh-dem-nhac-thuy-dung-km-nguyen-dinh-tuan-nghia",
#       "badge": None
#     },
#     {
#       "id": 13047,
#       "name": "WHITE PARTY VIETNAM 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/22/BF092B.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2024/02/18/AE4590.jpg",
#       "day": "2024-07-20T09:00:00Z",
#       "price": 2200000,
#       "deeplink": "https://ticketbox.vn/white-party-vietnam-89404-89404",
#       "isNewBookingFlow": True,
#       "originalId": 89404,
#       "url": "white-party-vietnam-89404",
#       "badge": None
#     },
#     {
#       "id": 22203,
#       "name": "[HN] TRUNG QUÂN  1689 - More than 1589",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/5d/61/dc/4ecd0c7c95090901b91c3cb2a62e2d85.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/be/d4/a4/b253a1a57ebce3d6e7ed7c427b8e13fd.jpg",
#       "day": "2024-07-26T12:00:00Z",
#       "price": 1000000,
#       "deeplink": "https://ticketbox.vn/hn-trung-quan-1689-more-than-1589-89911-89911",
#       "isNewBookingFlow": True,
#       "originalId": 89911,
#       "url": "hn-trung-quan-1689-more-than-1589-89911",
#       "badge": None
#     },
#     {
#       "id": 22693,
#       "name": "HARMONY FEST | ORANGE | GREY D | KAI ĐINH | BẢO ANH | CHILLIES",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/b4/3c/8e/7438bc6de1dd8995235e037f24877fc2.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/a4/a2/47/4fd97cc3a86342a8771b2e71d485c6f6.png",
#       "day": "2024-07-26T13:00:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/harmony-fest-orange-grey-d-kai-dinh-bao-anh-chillies-22693",
#       "isNewBookingFlow": True,
#       "originalId": 22693,
#       "url": "harmony-fest-orange-grey-d-kai-dinh-bao-anh-chillies",
#       "badge": None
#     },
#     {
#       "id": 22652,
#       "name": "LULULOLA SHOW THÙY CHI & MAI TIẾN DŨNG | NGƯỜI NHƯ ANH HƠN EM CHỖ NÀO",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/e9/fb/9b/4501e2de06f2b5f454dc35b119d24217.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/74b952cb0e06f18805e431406df4914e.jpg",
#       "day": "2024-07-27T10:30:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/lululola-thuy-chi-mai-tien-dung-22652",
#       "isNewBookingFlow": True,
#       "originalId": 22652,
#       "url": "lululola-thuy-chi-mai-tien-dung",
#       "badge": None
#     },
#     {
#       "id": 22484,
#       "name": "2024 SUPER JUNIOR \u003CSUPER SHOW SPIN-OFF: Halftime\u003E in HO CHI MINH",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/c2/4b/79/43aa7f8fbf384caa5ddceb011498dbd7.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/e8/9c/eb/4b586583297d6d7135a59210999ebf1b.png",
#       "day": "2024-07-28T10:00:00Z",
#       "price": 3000000,
#       "deeplink": "https://ticketbox.vn/super-show-spin-off-22484",
#       "isNewBookingFlow": True,
#       "originalId": 22484,
#       "url": "super-show-spin-off",
#       "badge": None
#     },
#     {
#       "id": 22630,
#       "name": "LULULOLA SHOW PHAN MẠNH QUỲNH | BIẾT ƠN ĐỂ ĐANG Ở LẠI",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/57/04/b1/39315e2c790f67ecc938701754816d15.png",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/fa/28/59/48b6c1d0c9fb73d067eb9f34c711410e.jpg",
#       "day": "2024-08-02T10:30:00Z",
#       "price": 450000,
#       "deeplink": "https://ticketbox.vn/phan-manh-quynh-22630",
#       "isNewBookingFlow": True,
#       "originalId": 22630,
#       "url": "phan-manh-quynh",
#       "badge": None
#     },
#   ],
# }

# # data = {
#   "results": [
#       {
#         "id": 759,
#         "name": "[Nhà Hát THANH NIÊN] Hài Kịch: Cuộc Chiến MENTOR",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/30/1d/f3/46af70adf10b12c5ef212a9221bef1c0.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2020/01/02/FFBC15.jpg",
#         "day": "2024-07-05T12:00:00Z",
#         "price": 180000,
#         "deeplink": "https://ticketbox.vn/kich-cuoc-chien-mentor-88862",
#         "isNewBookingFlow": True,
#         "originalId": 88862,
#         "url": "kich-cuoc-chien-mentor",
#         "badge": None
#       },
#       {
#         "id": 935,
#         "name": "[SÂN KHẤU THIÊN ĐĂNG]- VỞ KỊCH -LỘ HÀNG (LEAKED)",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/d5/be/68/a4574538116a50abf49c2a234cacf3d5.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2023/08/29/02E3E4.jpg",
#         "day": "2024-07-05T12:30:00Z",
#         "price": 330000,
#         "deeplink": "https://ticketbox.vn/san-khau-thien-dang-vo-kich-lo-hang-88085-88085",
#         "isNewBookingFlow": True,
#         "originalId": 88085,
#         "url": "san-khau-thien-dang-vo-kich-lo-hang-88085",
#         "badge": None
#       },
#       {
#         "id": 21484,
#         "name": "Sấn Khấu Hồng Vân: Quả Tim Máu (Phần 1)",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/76/04/17/15137642a5bed9b4ef2d30f6e0729ef8.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
#         "day": "2024-07-05T12:30:00Z",
#         "price": 250000,
#         "deeplink": "https://ticketbox.vn/san-khau-hong-van-qua-tim-mau-phan-1-89867-89867",
#         "isNewBookingFlow": True,
#         "originalId": 89867,
#         "url": "san-khau-hong-van-qua-tim-mau-phan-1-89867",
#         "badge": None
#       },
#       {
#         "id": 15089,
#         "name": "Nhà Hát Kịch IDECAF: MÁ ƠI ÚT DÌA!",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/75/97/51/7728fa71ce2776bb00203d46a8774de3.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2020/01/02/FFBC15.jpg",
#         "day": "2024-07-05T12:30:00Z",
#         "price": 150000,
#         "deeplink": "https://ticketbox.vn/kich-idecaf-ma-oi-ut-dia-89507",
#         "isNewBookingFlow": True,
#         "originalId": 89507,
#         "url": "kich-idecaf-ma-oi-ut-dia",
#         "badge": None
#       },
#       {
#         "id": 4977,
#         "name": "[VIVIAN VU’S CANDLES] WORKSHOP LÀM NẾN THƠM VÀ SÁP THƠM HANDMADE",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/01/09/187196.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2023/12/06/D29AF2.jpg",
#         "day": "2024-07-06T02:00:00Z",
#         "price": 315000,
#         "deeplink": "https://ticketbox.vn/workshop-lam-nen-thom-va-sap-thom-handmade-89039-89039",
#         "isNewBookingFlow": True,
#         "originalId": 89039,
#         "url": "workshop-lam-nen-thom-va-sap-thom-handmade-89039",
#         "badge": None
#       },
#       {
#         "id": 2899,
#         "name": "HÀ NỘI - PHÂN TÍCH NGHIỆP VỤ NÂNG CAO 3.0 (7, CN)",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/11/77/59/6c646c1e1ff1879808b7ddc1a20fad22.png",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2022/07/13/BCE47F.jpg",
#         "day": "2024-07-06T02:00:00Z",
#         "price": 7300000,
#         "deeplink": "https://ticketbox.vn/lop-phan-tich-nghiep-vu-phan-mem-nang-cao-ha-noi-80741",
#         "isNewBookingFlow": True,
#         "originalId": 80741,
#         "url": "lop-phan-tich-nghiep-vu-phan-mem-nang-cao-ha-noi",
#         "badge": None
#       },
#       {
#         "id": 13530,
#         "name": "[NEW] Moss Frame Workshop",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/20/5E5057.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
#         "day": "2024-07-06T03:00:00Z",
#         "price": 450000,
#         "deeplink": "https://ticketbox.vn/moss-frame-workshop-89427-89427",
#         "isNewBookingFlow": True,
#         "originalId": 89427,
#         "url": "moss-frame-workshop-89427",
#         "badge": None
#       },
#       {
#         "id": 22520,
#         "name": "Tình Bạn Diệu Kỳ - Only Friends Fanmeeting in VietNam",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/95/a6/34/d948a3b57b4d39c2aaed17b8d8c6f925.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/cd/99/06/62fe7c57c1f2e8c3efa70d1e0e263276.jpg",
#         "day": "2024-07-06T07:00:00Z",
#         "price": 2200000,
#         "deeplink": "https://ticketbox.vn/only-friends-fanmeeting-22520",
#         "isNewBookingFlow": True,
#         "originalId": 22520,
#         "url": "only-friends-fanmeeting",
#         "badge": None
#       },
#       {
#         "id": 14351,
#         "name": "[NEW]Workshop thư pháp \"Nét Bình Yên\"",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/24/8D2BA4.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2024/02/24/665F0F.jpg",
#         "day": "2024-07-06T07:00:00Z",
#         "price": 350000,
#         "deeplink": "https://ticketbox.vn/workshop-thu-phap-net-binh-yen-89456-89456",
#         "isNewBookingFlow": True,
#         "originalId": 89456,
#         "url": "workshop-thu-phap-net-binh-yen-89456",
#         "badge": None
#       },
#       {
#         "id": 14359,
#         "name": "[NEW]Kokedama Workshop",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/24/D72959.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2024/02/24/8F71AB.jpg",
#         "day": "2024-07-06T08:00:00Z",
#         "price": 350000,
#         "deeplink": "https://ticketbox.vn/kokedama-workshop-89457-89457",
#         "isNewBookingFlow": True,
#         "originalId": 89457,
#         "url": "kokedama-workshop-89457",
#         "badge": None
#       },
#       {
#         "id": 22433,
#         "name": "[Sân Khấu Quốc Thảo] Nhạc kịch thiếu nhi: Đảo Muôn Màu & Cuộc Thử Thách Sinh Tồn",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/99/06/38/2ab39477e1179236ade8dc3736b6a84b.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/01/a3/dc/b2c9b46186e391badfeac2f3a0f58861.png",
#         "day": "2024-07-06T12:00:00Z",
#         "price": 80000,
#         "deeplink": "https://ticketbox.vn/san-khau-quoc-thao-dao-muon-mau-22433",
#         "isNewBookingFlow": True,
#         "originalId": 22433,
#         "url": "san-khau-quoc-thao-dao-muon-mau",
#         "badge": None
#       },
#       {
#         "id": 19899,
#         "name": "Nhà Hát Kịch IDECAF: NXNX35 - Huyền Thoại Mắt Thần",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/7d/bf/29/ba72bc82311fc26f58b979ccab54d4d9.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/7d/fc/85/481ef3de9970b4bf4abe2a23e32da2ba.png",
#         "day": "2024-07-06T12:00:00Z",
#         "price": 250000,
#         "deeplink": "https://ticketbox.vn/kich-idecaf-ngay-xua-ngay-xua-35-89765",
#         "isNewBookingFlow": True,
#         "originalId": 89765,
#         "url": "kich-idecaf-ngay-xua-ngay-xua-35",
#         "badge": None
#       },
#       {
#         "id": 307,
#         "name": "SÂN KHẤU 5B : BỒ CÔNG ANH",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2020/06/03/AA1C75.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2020/05/14/DA6270.jpg",
#         "day": "2024-07-06T12:00:00Z",
#         "price": 250000,
#         "deeplink": "https://ticketbox.vn/kich-bo-cong-anh-5b-vo-van-tan-79678",
#         "isNewBookingFlow": True,
#         "originalId": 79678,
#         "url": "kich-bo-cong-anh-5b-vo-van-tan",
#         "badge": None
#       },
#       {
#         "id": 42,
#         "name": "SÂN KHẤU THIÊN ĐĂNG -VỞ KỊCH : GIÁNG HƯƠNG",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/7c/9e/e9/573f9a55794e30964908a20f06d629a2.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/Upload/organizerlogo/2023/08/15/99DD16.jpg",
#         "day": "2024-07-06T12:30:00Z",
#         "price": 330000,
#         "deeplink": "https://ticketbox.vn/san-khau-thien-dang-kich-giang-huong-88063",
#         "isNewBookingFlow": True,
#         "originalId": 88063,
#         "url": "san-khau-thien-dang-kich-giang-huong",
#         "badge": None
#       },
#       {
#         "id": 16096,
#         "name": "Sân Khấu Hồng Vân: Vở Kịch Người Vợ Ma",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/06/C27495.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
#         "day": "2024-07-06T12:30:00Z",
#         "price": 250000,
#         "deeplink": "https://ticketbox.vn/san-khau-hong-van-vo-kich-nguoi-vo-ma-89557-89557",
#         "isNewBookingFlow": True,
#         "originalId": 89557,
#         "url": "san-khau-hong-van-vo-kich-nguoi-vo-ma-89557",
#         "badge": None
#       },
#       {
#         "id": 22401,
#         "name": "Vở cải lương \"Đêm trước ngày hoàng đạo\"",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/07/97/6f/6a99178abfbddca64b3ee302b595a949.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/ca/38/c5/553adf6906ebfbedb390a8f8c57614ad.jpg",
#         "day": "2024-07-06T13:00:00Z",
#         "price": 200000,
#         "deeplink": "https://ticketbox.vn/vo-cai-luong-dem-truoc-ngay-hoang-dao-22401",
#         "isNewBookingFlow": True,
#         "originalId": 22401,
#         "url": "vo-cai-luong-dem-truoc-ngay-hoang-dao",
#         "badge": None
#       },
#       {
#         "id": 22626,
#         "name": "WORKSHOP VẼ TRANH CANVAS \"GAM MÀU HẠNH PHÚC - COLOR OF JOY\"",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/3d/56/d0/1953b6e8bdb089a3fd54b5f7363f1d61.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/af/67/3b/4f23875375628a3d07d54b7b67239848.png",
#         "day": "2024-07-07T02:00:00Z",
#         "price": 220000,
#         "deeplink": "https://ticketbox.vn/workshop-gam-mau-hanh-phuc-color-of-joy-22626",
#         "isNewBookingFlow": True,
#         "originalId": 22626,
#         "url": "workshop-gam-mau-hanh-phuc-color-of-joy",
#         "badge": None
#       },
#       {
#         "id": 22634,
#         "name": "SÂN KHẤU 5B : TRẠM CỨU HỘ ĐỘNG VẬT",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/93/17/38/c1f681c6a360754fcb9ef908d357a872.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/9c/4e/57/0ca01ea9c9c0a37e6063b0d6a8123523.jpg",
#         "day": "2024-07-07T03:00:00Z",
#         "price": 250000,
#         "deeplink": "https://ticketbox.vn/san-khau-5b-tram-cuu-ho-dong-vat-22634",
#         "isNewBookingFlow": True,
#         "originalId": 22634,
#         "url": "san-khau-5b-tram-cuu-ho-dong-vat",
#         "badge": None
#       },
#       {
#         "id": 22629,
#         "name": "PIANO RECITAL - SOUNDS OF YOUTH",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/bc/bc/d7/7768dfe312efa1fdd899762d954eb40d.jpg",
#         "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/9e/a0/c4/3bee96cd754c4fd3e9e8ef473cb1d158.jpg",
#         "day": "2024-07-07T03:00:00Z",
#         "price": 150000,
#         "deeplink": "https://ticketbox.vn/piano-recital-sounds-of-youth-22629",
#         "isNewBookingFlow": True,
#         "originalId": 22629,
#         "url": "piano-recital-sounds-of-youth",
#         "badge": None
#       },
#       {
#         "id": 14281,
#         "name": "[NEW]Stress Breaker Workshop",
#         "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/24/FE522F.jpg",
#         "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2024/02/24/F97DBD.jpg",
#         "day": "2024-07-07T03:00:00Z",
#         "price": 375000,
#         "deeplink": "https://ticketbox.vn/stress-breaker-89454",
#         "isNewBookingFlow": True,
#         "originalId": 89454,
#         "url": "stress-breaker",
#         "badge": None
#       }
#     ],
# }

# data = {
#   "results": [
#     {
#       "id": 22698,
#       "name": "VBA  2024 - SAIGON HEAT VS HANOI BUFFALOES - JUL 07",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/57edbec5b30f821eadb74bdabef9c565.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/343cbb0625faf87d74149b59394e3d89.png",
#       "day": "2024-07-07T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heats-vs-hanoi-buffaloes-22698",
#       "isNewBookingFlow": True,
#       "originalId": 22698,
#       "url": "vba-2024-saigon-heats-vs-hanoi-buffaloes",
#       "badge": None
#     },
#     {
#       "id": 22681,
#       "name": "Lion Championship 15 - 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/16/80/7e/44d46d5e87b1ff7c207251ee6e4ad5df.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/08/63/d6/e2b991ef85fde1ce73cc7d68a791decf.jpg",
#       "day": "2024-07-13T07:00:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/lion-championship-15-2024-22681",
#       "isNewBookingFlow": True,
#       "originalId": 22681,
#       "url": "lion-championship-15-2024",
#       "badge": None
#     },
#     {
#       "id": 22700,
#       "name": "VBA 2024 - SAIGON HEAT VS DANANG DRAGONS - JUL 14",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/5133b985ec3f90d08ee604ca129e6920.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/93c0a6ce7f7a01b458954965b04fea07.png",
#       "day": "2024-07-14T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-da-nang-dragons-22700",
#       "isNewBookingFlow": True,
#       "originalId": 22700,
#       "url": "vba-2024-saigon-heat-vs-da-nang-dragons",
#       "badge": None
#     },
#     {
#       "id": 22701,
#       "name": "VBA  2024 - SAIGON HEAT VS CANTHO CATFISH - JUL 17",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/c5709e986a5d39ebbdfb73e2a11b8d00.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/b76dcff97d5b36e2f172fd83fcab11d9.png",
#       "day": "2024-07-17T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-cantho-catfish-22701",
#       "isNewBookingFlow": True,
#       "originalId": 22701,
#       "url": "vba-2024-saigon-heat-vs-cantho-catfish",
#       "badge": None
#     },
#     {
#       "id": 22704,
#       "name": "VBA  2024 - SAIGON HEAT VS HO CHI MINH CITY WINGS - JUL 19",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/086c7352a3a7caa5e150e5dc22dbe424.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/efa6d75609d4eb8447936be85d5dd56d.png",
#       "day": "2024-07-19T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-ho-chi-minh-city-wings-22704",
#       "isNewBookingFlow": True,
#       "originalId": 22704,
#       "url": "vba-2024-saigon-heat-vs-ho-chi-minh-city-wings",
#       "badge": None
#     },
#     {
#       "id": 22570,
#       "name": "Muay Thai Rampage x Road To ONE: Vietnam - SEMI-FINAL ROUND/ VÒNG BÁN KẾT",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/26/57/6f/4640e05173bc98583fe3117ea0a29172.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/5f/4a/7a/4a651ef912927b9debf01c06416bc4be.png",
#       "day": "2024-07-21T11:00:00Z",
#       "price": 300000,
#       "deeplink": "https://ticketbox.vn/muaythairampage-roadtoone-22570",
#       "isNewBookingFlow": True,
#       "originalId": 22570,
#       "url": "muaythairampage-roadtoone",
#       "badge": None
#     },
#     {
#       "id": 22708,
#       "name": "VBA  2024 - SAIGON HEAT VS DANANG DRAGONS - JUL 28",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/73042ae6ca1adea02103d5eda99264fc.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/1117f337cb8d4d7f47d5bf84e35ae712.png",
#       "day": "2024-07-28T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-danang-dragons-22708",
#       "isNewBookingFlow": True,
#       "originalId": 22708,
#       "url": "vba-2024-saigon-heat-vs-danang-dragons",
#       "badge": None
#     },
#     {
#       "id": 22709,
#       "name": "VBA  2024 - SAIGON HEAT VS NHA TRANG DOLPHINS - AUG 07",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/d5fcba94a5390448be39e32f22519b31.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/563bb18a33a5a57d76bedd9c4b6d427d.png",
#       "day": "2024-08-07T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-nha-trang-dolphins-aug-07-22709",
#       "isNewBookingFlow": True,
#       "originalId": 22709,
#       "url": "vba-2024-saigon-heat-vs-nha-trang-dolphins-aug-07",
#       "badge": None
#     },
#     {
#       "id": 22710,
#       "name": "VBA  2024 - SAIGON HEAT VS NHA TRANG DOLPHINS - AUG 10",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/faf7434e7629fb90c46441b1b4e74404.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/4da4c339e0fc4c6f83b59a874ad264de.png",
#       "day": "2024-08-10T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-nha-trang-dolphins-aug-10-22710",
#       "isNewBookingFlow": True,
#       "originalId": 22710,
#       "url": "vba-2024-saigon-heat-vs-nha-trang-dolphins-aug-10",
#       "badge": None
#     },
#     {
#       "id": 22711,
#       "name": "VBA  2024 - SAIGON HEAT VS CAN THO CATFISH - AUG 31",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/bc9b81311df14f239d727191f6712132.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/2c4326fc51b38cef0af50bff512c1013.png",
#       "day": "2024-08-31T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-can-tho-catfish-aug-31-22711",
#       "isNewBookingFlow": True,
#       "originalId": 22711,
#       "url": "vba-2024-saigon-heat-vs-can-tho-catfish-aug-31",
#       "badge": None
#     },
#     {
#       "id": 22677,
#       "name": "VBA 2024 - SAIGON HEAT VS HANOI BUFFALOES- JUNE 30",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/a348aaf8011d4cb464f33f7a4d29eda6.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/b865c8b39392cb1fcb279593f5dafce9.png",
#       "day": "2024-06-30T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-saigon-heat-vs-hanoi-buffaloes-22677",
#       "isNewBookingFlow": True,
#       "originalId": 22677,
#       "url": "vba-2024-saigon-heat-vs-hanoi-buffaloes",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 22676,
#       "name": "VBA  2024 - SAIGON HEAT VS HO CHI MINH WINGS - JUNE 28",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9b/70/96/2dd7c9300a46215dcc8df0cb5b83aac6.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/52/3d/58/d6714750f6f6179d4eb5730df6d934b6.png",
#       "day": "2024-06-28T12:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/vba-2024-sai-gon-heat-ho-chi-minh-wings-22676",
#       "isNewBookingFlow": True,
#       "originalId": 22676,
#       "url": "vba-2024-sai-gon-heat-ho-chi-minh-wings",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 22552,
#       "name": "Lion Championship 14 - 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/ee/f4/b3/2c2c4b30ec43fa6a526f6be777203dfa.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c8/2d/6d/491250abe2c66d1bff16716c61712178.jpg",
#       "day": "2024-06-15T11:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/lionchampionship14-22552",
#       "isNewBookingFlow": True,
#       "originalId": 22552,
#       "url": "lionchampionship14",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 14124,
#       "name": "MuayThai Rampage x Road to One - ELIMINATION",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/5e/d6/a3/b03f1c63cf18affcd298bc2252f8dba5.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/73/e9/10/b634bf886fe20f43b78fc42a15749614.jpg",
#       "day": "2024-05-19T11:00:00Z",
#       "price": 300000,
#       "deeplink": "https://ticketbox.vn/muaythai-rampage-road-to-one-89452-89452",
#       "isNewBookingFlow": True,
#       "originalId": 89452,
#       "url": "muaythai-rampage-road-to-one-89452",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 22483,
#       "name": "VIEWING PARTY - CHUNG KẾT TỔNG MSI 2024 | TPHCM & HÀ NỘI",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/a1/11/1e/61860cba92c1153a0e5a21190d7bea8b.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/39/01/55/b731be0bb461a685f5fee1e581b72ee3.png",
#       "day": "2024-05-19T08:00:00Z",
#       "price": 129000,
#       "deeplink": "https://ticketbox.vn/chung-ket-msi-2024-22483",
#       "isNewBookingFlow": True,
#       "originalId": 22483,
#       "url": "chung-ket-msi-2024",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 22421,
#       "name": "Lion Championship 13 - 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/d7/47/bb/96e77130a842e86eef4b59b79469b7e9.jpg",
#       "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/98/9f/4a/97eae4a1bbf70b99c4df5bf03a8f4d9f.jpg",
#       "day": "2024-05-18T11:30:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/lionchampionship13-22421",
#       "isNewBookingFlow": True,
#       "originalId": 22421,
#       "url": "lionchampionship13",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 17374,
#       "name": "BRAZIL VIETNAM FOOTBALL FESTIVAL 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/04/22/B17195.jpg",
#       "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2024/03/27/967160.jpg",
#       "day": "2024-04-27T10:00:00Z",
#       "price": 600000,
#       "deeplink": "https://ticketbox.vn/brazil-vietnam-football-festival-2023-89635-89635",
#       "isNewBookingFlow": True,
#       "originalId": 89635,
#       "url": "brazil-vietnam-football-festival-2023-89635",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 18839,
#       "name": "Lion Championship 12 - 2024",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/25/96AFC5.jpg",
#       "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
#       "day": "2024-04-13T08:00:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/lion-championship-12-2024-89706",
#       "isNewBookingFlow": True,
#       "originalId": 89706,
#       "url": "lion-championship-12-2024",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 12587,
#       "name": "FreenBecky 1st Fan Meeting in Vietnam",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/07/64C32B.jpg",
#       "orgLogoUrl": "https://static.tkbcdn.com/Upload/organizerlogo/2024/02/07/C2678C.jpg",
#       "day": "2024-03-30T06:00:00Z",
#       "price": 1800000,
#       "deeplink": "https://ticketbox.vn/freenbecky-fan-meeting-in-vietnam-89390-89390",
#       "isNewBookingFlow": True,
#       "originalId": 89390,
#       "url": "freenbecky-fan-meeting-in-vietnam-89390",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     },
#     {
#       "id": 12388,
#       "name": "Ecstatic Dance Saigon",
#       "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/02/02/4FB3DD.jpg",
#       "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
#       "day": "2024-03-17T10:00:00Z",
#       "price": 200000,
#       "deeplink": "https://ticketbox.vn/ecstatic-dance-saigon-89377",
#       "isNewBookingFlow": True,
#       "originalId": 89377,
#       "url": "ecstatic-dance-saigon",
#       "badge": {
#         "label": {
#           "vi": "Đã diễn ra",
#           "en": "Event over"
#         },
#         "backgroundColor": "#FC820A",
#         "textColor": "#FFFFFF"
#       }
#     }
#   ],
# }

data = {
  "results": [
      {
        "id": 22426,
        "name": "CHƯƠNG TRÌNH TỊNH KHẨU tháng 07",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/1a/2c/7e/cc350dbace0ed52b8529473132bae6e1.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/65/f8/de/bbfb950a368cdc19251e9b208fa40b5e.png",
        "day": "2024-07-04T07:00:00Z",
        "price": 600000,
        "deeplink": "https://ticketbox.vn/chuong-trinh-tinh-khau-t7-2024-22426",
        "isNewBookingFlow": True,
        "originalId": 22426,
        "url": "chuong-trinh-tinh-khau-t7-2024",
        "badge": None
      },
      {
        "id": 21816,
        "name": "[THE GREENERY ART] WORKSHOP \"BÁNH KEM ĐẬU NÀNH ĐÀI LOAN\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/74/80/a8/4855e27874d84d3bd7d8db32e9830d86.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/1eb538134855d000e06fd5b25bf807ba.png",
        "day": "2024-07-04T07:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-banh-kem-dau-nanh-dai-loan-89891",
        "isNewBookingFlow": True,
        "originalId": 89891,
        "url": "the-greenery-art-workshop-banh-kem-dau-nanh-dai-loan",
        "badge": None
      },
      {
        "id": 22407,
        "name": "[THE GREENERY ART] WORKSHOP \"LY NẾN BIỂN - OCEAN SCENTED CANDLE\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/d0/fb/f4/e12bc31c00a9a2084bc255e19a0d532e.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/608594484a519c5a977325ace886d85a.png",
        "day": "2024-07-04T07:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/ly-nen-bien-22407",
        "isNewBookingFlow": True,
        "originalId": 22407,
        "url": "ly-nen-bien",
        "badge": None
      },
      {
        "id": 16859,
        "name": "[NEW]Workshop Leaf Leather Engraving - Khắc Lá Da",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/Upload/eventcover/2024/03/12/D16847.jpg",
        "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
        "day": "2024-07-04T08:00:00Z",
        "price": 350000,
        "deeplink": "https://ticketbox.vn/workshop-leaf-leather-engraving-khac-la-da-89611-89611",
        "isNewBookingFlow": True,
        "originalId": 89611,
        "url": "workshop-leaf-leather-engraving-khac-la-da-89611",
        "badge": None
      },
      {
        "id": 22667,
        "name": "Chuỗi Chương Trình Phi Lợi Nhuận Về Phát Triển Bản Thân: TÔI - PHIÊN BẢN KẾT NỐI",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/d4/02/28/1631323dba06301ad814c165846cb4a9.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/50/52/1c/3c169cd018eaccacf3916e6ccb8a6e3d.jpg",
        "day": "2024-07-04T10:00:00Z",
        "price": 0,
        "deeplink": "https://ticketbox.vn/chuoi-chuong-trinh-phi-loi-nhuan-ve-phat-trien-ban-than-toi-phien-ban-ket-noi-22667",
        "isNewBookingFlow": True,
        "originalId": 22667,
        "url": "chuoi-chuong-trinh-phi-loi-nhuan-ve-phat-trien-ban-than-toi-phien-ban-ket-noi",
        "badge": None
      },
      {
        "id": 21714,
        "name": "[THE GREENERY ART] WORKSHOP \"VẼ TRANH MÀU NƯỚC - WATERCOLOR PAINTING\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/e5/70/33/6cb8ec72fe51f64a4491e82256ecbeb2.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/fc3ab525b71fa0ab0eff8116d50165dd.png",
        "day": "2024-07-04T10:30:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-ve-tranh-mau-nuoc-watercolor-painting-89884-89884",
        "isNewBookingFlow": True,
        "originalId": 89884,
        "url": "the-greenery-art-workshop-ve-tranh-mau-nuoc-watercolor-painting-89884",
        "badge": None
      },
      {
        "id": 19533,
        "name": "[THE GREENERY ART] WORKSHOP \"BÁNH QUY MOCHI\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/a9/db/08/1b52a0f3dbbd60ec08a1051cc1f588cd.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/8a1eadc94efa0899c8af297636199f11.png",
        "day": "2024-07-04T10:30:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-banh-quy-mochi-89750-89750",
        "isNewBookingFlow": True,
        "originalId": 89750,
        "url": "the-greenery-art-workshop-banh-quy-mochi-89750",
        "badge": None
      },
      {
        "id": 21503,
        "name": "[THE GREENERY ART] WORKSHOP \"TRANH LEN DÁN - WOOL PICTURE\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/13/d9/ab/a17d6004eb1abec6ab7e52c01c17198a.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/909646e0e78a89b87ec77335099c850b.png",
        "day": "2024-07-05T03:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-tranh-len-dan-wool-picture-89871",
        "isNewBookingFlow": True,
        "originalId": 89871,
        "url": "the-greenery-art-workshop-tranh-len-dan-wool-picture",
        "badge": None
      },
      {
        "id": 21651,
        "name": "[THE GREENERY ART] WORKSHOP \"MINI TART TRÁI CÂY - FRUIT MINI TART\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/7e/49/4c/518a3e6c12a767adaaa2aabc31c6363f.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/317aa08bde1a3c2f630ea4e42a06b403.png",
        "day": "2024-07-05T03:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-fruit-mini-tart-2024-89880-89880",
        "isNewBookingFlow": True,
        "originalId": 89880,
        "url": "the-greenery-art-workshop-fruit-mini-tart-2024-89880",
        "badge": None
      },
      {
        "id": 22415,
        "name": "[THE GREENERY ART] WORKSHOP BÁNH \"MOCHI CHEESECAKE\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/a1/f6/96/bbe14b64669540c231fae51adb1457d6.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/7ac89db661ac44b3edf48b307820e4e1.png",
        "day": "2024-07-05T07:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/mochi-cheesecake-22415",
        "isNewBookingFlow": True,
        "originalId": 22415,
        "url": "mochi-cheesecake",
        "badge": None
      },
      {
        "id": 21694,
        "name": "[THE GREENERY ART] WORKSHOP \"TINH DẦU KHUẾCH TÁN - ESSENTIAL OIL REED DIFFUSERS\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/5c/8f/51/430b1cfe96e9db656c3a37aa98f3c30e.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/6c3e0eb0c058e5eb62f67e63e5aa5dd0.png",
        "day": "2024-07-05T07:00:00Z",
        "price": 440000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-workshop-tinh-dau-khuech-tan-essential-oil-reed-diffusers-89883",
        "isNewBookingFlow": True,
        "originalId": 89883,
        "url": "the-greenery-art-workshop-tinh-dau-khuech-tan-essential-oil-reed-diffusers",
        "badge": None
      },
      {
        "id": 22452,
        "name": "[THE GREENERY ART] WORKSHOP \"VẼ TRANH CANVAS - CANVAS PAINTING\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/b4/9f/72/a49fc634754b99c78669075f425ae3cd.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/c53b6ca4fea75bb9e39cf78562e4cf97.png",
        "day": "2024-07-05T10:30:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/ve-tranh-canvas-22452",
        "isNewBookingFlow": True,
        "originalId": 22452,
        "url": "ve-tranh-canvas",
        "badge": None
      },
      {
        "id": 22543,
        "name": "[THE GREENERY ART] WORKSHOP BÁNH \"MOCHI DONUT\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/2b/ea/2e/59bdbe1f22c3df04f8c99e61e62e206f.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/62d0f4be88dd99cca226cf9fcc0a3cb7.png",
        "day": "2024-07-05T10:30:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/mochi-donut-22543",
        "isNewBookingFlow": True,
        "originalId": 22543,
        "url": "mochi-donut",
        "badge": None
      },
      {
        "id": 16894,
        "name": "[NEW]Workshop Fairy Dome - Vòm Tiên",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/9e/b1/45/ea142d92432e82e3983a6c18a8bb2188.jpeg",
        "orgLogoUrl": "https://static.tkbcdn.com/Upload/avatar.png",
        "day": "2024-07-05T11:00:00Z",
        "price": 395000,
        "deeplink": "https://ticketbox.vn/workshop-fairy-dome-vom-tien-89615-89615",
        "isNewBookingFlow": True,
        "originalId": 89615,
        "url": "workshop-fairy-dome-vom-tien-89615",
        "badge": None
      },
      {
        "id": 22586,
        "name": "[9X GARDEN] Workshop Broken Pot, New Life - Điều kỳ diệu từ mảnh vỡ",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/cf/6b/e2/9d9aa12bdb9f9dd8acf0b7e3498ba984.png",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/29/e8/1659950849f2e8e5eee3e44eac25a4e8.png",
        "day": "2024-07-06T02:00:00Z",
        "price": 349000,
        "deeplink": "https://ticketbox.vn/workshop-brokenpot-22586",
        "isNewBookingFlow": True,
        "originalId": 22586,
        "url": "workshop-brokenpot",
        "badge": None
      },
      {
        "id": 22690,
        "name": "[FLOWER 1969’s] WORKSHOP SCENTED RELIEF SCULPTURES - PHÙ ĐIÊU HƯƠNG",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/1e/39/1d/874c4876d28e061e693f564e09e2d338.png",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/b9/bd/d6/ac6e0afc54e5d73009108f246c3fed03.png",
        "day": "2024-07-06T03:00:00Z",
        "price": 323000,
        "deeplink": "https://ticketbox.vn/flower-1969s-workshop-scented-relief-sculptures-phu-dieu-huong-22690",
        "isNewBookingFlow": True,
        "originalId": 22690,
        "url": "flower-1969s-workshop-scented-relief-sculptures-phu-dieu-huong",
        "badge": None
      },
      {
        "id": 22408,
        "name": "[THE GREENERY ART] WORKSHOP \"TỤ NẾN ĐẠI DƯƠNG - OCEAN DECORATIVE CANDLE\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/0e/13/1b/a50ded24c44a0d2297f254f36812d28b.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/feaeb766ab8511701500fa0af7f345b4.png",
        "day": "2024-07-06T03:00:00Z",
        "price": 550000,
        "deeplink": "https://ticketbox.vn/tu-nen-dai-duong-22408",
        "isNewBookingFlow": True,
        "originalId": 22408,
        "url": "tu-nen-dai-duong",
        "badge": None
      },
      {
        "id": 19531,
        "name": "[THE GREENERY ART] ART WORKSHOP \"LEMON SHORTCAKE\"",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/eb/74/4e/8f56c9d9416ae4c57396b41f5f958562.jpg",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/c4/48/c8/29e5a4d2d093d8b8a0c24278ac4e5935.png",
        "day": "2024-07-06T03:00:00Z",
        "price": 385000,
        "deeplink": "https://ticketbox.vn/the-greenery-art-art-workshop-lemon-shortcake-89749",
        "isNewBookingFlow": True,
        "originalId": 89749,
        "url": "the-greenery-art-art-workshop-lemon-shortcake",
        "badge": None
      },
      {
        "id": 22275,
        "name": "[FLOWER 1969’s] GEL SOAP WORKSHOP - XÀ PHÒNG GEL TRONG",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/11/d7/ea/71c1c6f1beec396bbf85af8526ebed36.png",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/b9/bd/d6/b0c31e9725885d36df0967b6a7be8d30.png",
        "day": "2024-07-06T07:00:00Z",
        "price": 277000,
        "deeplink": "https://ticketbox.vn/flower-1969s-gel-soap-workshop-hoc-lam-xa-phong-gel-trong-89924",
        "isNewBookingFlow": True,
        "originalId": 89924,
        "url": "flower-1969s-gel-soap-workshop-hoc-lam-xa-phong-gel-trong",
        "badge": None
      },
      {
        "id": 1344,
        "name": "[FLOWER 1969’s] SOAP WORKSHOP - HỌC LÀM XÀ PHÒNG",
        "imageUrl": "https://images.tkbcdn.com/2/608/332/ts/ds/22/a3/bd/cb16e7c4284036d703ff22dd9dea1266.png",
        "orgLogoUrl": "https://salt.tkbcdn.com/ts/ds/b9/bd/d6/0b9baa309f50d5360f526bc88577cb4e.png",
        "day": "2024-07-06T07:00:00Z",
        "price": 278000,
        "deeplink": "https://ticketbox.vn/flower-1696s-workshop-xa-phong-83837",
        "isNewBookingFlow": True,
        "originalId": 83837,
        "url": "flower-1696s-workshop-xa-phong",
        "badge": None
      }
    ],
}

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # assuming 'root' is your username
    password="123",  # your password
    database="event_management"
)

cursor = db.cursor()

# Insert data into the database
for event in data["results"]:
    name = event["name"]
    datetime_str = event["day"].replace("T", " ").replace("Z", "")
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    price = event["price"]
    bannerURL = event["imageUrl"]
    categories = "other"
    location = random.choice(["Hồ Chí Minh", "Hà Nội"])
    
    sql = "INSERT INTO Events (name, datetime, minTicketPrice, bannerURL, categories, location) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, datetime_obj, price, bannerURL, categories, location)
    
    cursor.execute(sql, values)

db.commit()

cursor.close()
db.close()
