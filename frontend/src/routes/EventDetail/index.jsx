import { useNavigate, useParams } from "react-router-dom";
import styles from "./Event.module.css";
import { Typography } from "@mui/material";
import { useEffect, useState } from "react";

const data = {
  Events: [
    {
      id: 1,
      name: "[Sài Gòn] Những Thành Phố Mơ Màng Summer Tour 2024",
      description:
        '\u003Ch1 class="p1" style="text-align: center;"\u003ENhững Thành Phố Mơ Màng - Summer Hà Nội 2024\u003C/h1\u003E\n\u003Cp class="p1"\u003ECư dân đã sẵn sàng chuẩn bị cho chuyến hành trình với &#34;Những Thành Phố Mơ Màng Summer&#34; chưa! Đón nhận không khí trẻ trung, năng động của mùa hè, sự lung linh của thành phố, và những bản hit âm nhạc sôi động. Hãy mua ngay vé để trải nghiệm cuộc phiêu lưu âm nhạc độc đáo này và tận hưởng một mùa hè đầy ý nghĩa cùng NTPMM nhé.\u003C/p\u003E\n\u003Cul\u003E\n\u003Cli class="p1" style="font-style: italic;"\u003E\u003Cem\u003EThời gian: 06/07/2024 \u003C/em\u003E\u003C/li\u003E\n\u003Cli class="p1" style="font-style: italic;"\u003E\u003Cem\u003EĐịa điểm: Cung Điền Kinh Mỹ Đình, Hà Nội (Khu vực trong nhà)\u003C/em\u003E\u003C/li\u003E\n\u003C/ul\u003E\n\u003Ch2\u003ESƠ ĐỒ SỰ KIỆN\u003C/h2\u003E\n\u003Cp\u003E\u003Cimg src="https://salt.tkbcdn.com/ts/ds/99/04/88/3cf3cab9f5d50cf81a385f994217c43d.jpg" alt="" width="1413" height="1413"\u003E\u003C/p\u003E\n\u003Ch2 class="p2"\u003E\u003Cstrong\u003EQUY ĐỊNH MUA VÉ\u003C/strong\u003E\u003C/h2\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 1. Chương trình dành cho đối tượng khán giả trên 16 tuổi. Khán giả từ 10-15 tuổi tham gia chương trình phải có người giám hộ đi kèm (người giám hộ phải từ 18 tuổi trở lên, một người giám hộ kèm một trẻ vị thành niên) để quản lý và chịu hoàn toàn trách nhiệm nếu có bất kỳ sự cố nào xảy ra trong sự kiện.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 2. Phụ nữ mang thai và người có vấn đề về sức khoẻ tự cân nhắc khi tham gia chương trình. Trong trường hợp có vấn đề xảy ra, BTC không chịu trách nhiệm.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 3. Mỗi vé chỉ dành cho một khán giả tham dự, không kèm trẻ em và trẻ vị thành niên. Người giám hộ đi kèm theo khán giả vị thành niên phải mua vé để tham dự. \u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 4. Vé đã mua không được đổi hoặc hoàn trả dưới mọi hình thức. Khán giả có trách nhiệm tự bảo quản, bảo mật thông tin mã vé của mình. BTC từ chối giải quyết trường hợp có nhiều hơn một người check-in cùng một mã vé. Theo quy định, BTC cho phép người check-in đầu tiên mã vé bị trùng được tham dự sự kiện.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 5. Vui lòng không mua vé từ bất kỳ nguồn nào khác ngoài Ticketbox tránh trường hợp vé giả hoặc lừa đảo. BTC từ chối giải quyết cho những trường hợp mua vé từ nguồn khác nếu có vấn đề hay tranh chấp xảy ra.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 6. Khi tham gia chương trình, khán giả đồng ý với việc hình ảnh của mình được sử dụng để khai thác cho sản phẩm ghi hình, thu âm, quảng bá cho chương trình.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 7. BTC có quyền kiểm tra giấy tờ tùy thân của khán giả nếu có nghi ngờ về độ tuổi không phù hợp và từ chối quyền tham gia của bất kì khán giả nào không tuân thủ quy định của chương trình mà không hoàn trả vé.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 8. BTC có thể hoãn, hủy hoặc tạm ngưng sự kiện do vấn đề bất lợi về thời tiết, tình huống khẩn cấp hoặc nguy hiểm (trường hợp bất khả kháng hoặc nằm ngoài tầm kiểm soát của BTC). Trong trường hợp như trên, phương án đảm bảo quyền lợi cho khán giả đã mua vé sẽ được thực hiện theo quyết định của BTC. \u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 9. Khán giả tham dự sự kiện phải tự ý thức và có trách nhiệm bảo vệ sức khoẻ của bản thân khi tham gia. Khi tham gia show đồng nghĩa với việc khán giả đã cân nhắc về các vấn đề bao gồm điều kiện thời tiết bất lợi trước, trong hoặc sau sự kiện, các rủi ro từ tình trạng sức khỏe hiện có hoặc trong quá trình di chuyển đi và đến từ địa điểm.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 10. Trong mọi trường hợp, quyết định của BTC là quyết định cuối cùng.\u003C/p\u003E\n\u003Cp dir="ltr" dir="ltr"\u003EĐiều 11. Vui lòng theo dõi thêm và tuân thủ các quy định cũng như những đồ dùng bị cấm mang sẽ được đăng tải tại trang Facebook của chương trình trước khi chương trình được diễn ra.\u003C/p\u003E\n\u003Cp class="p1"\u003E \u003C/p\u003E',
      location: "Việt Nam, Phường Tân Phú, Quận 7, Thành Phố Hồ Chí Minh",
      datetime: "2024-06-15 07:30:00",
      bannerURL:
        "https://salt.tkbcdn.com/ts/ds/9f/0b/d4/f19a8a171d730418077d310ff82e7224.jpg",
      url: "ntpmmhochiminh-2024-89509",
      venue: "Trung Tâm Hội Chợ Triển Lãm Sài Gòn SECC",
      address: "Việt Nam, Phường Tân Phú, Quận 7, Thành Phố Hồ Chí Minh",
      orgId: 1,
      minTicketPrice: 550000,
      status: "event_over",
      statusName: "Sự kiện đã kết thúc",
      categories: '["music"]',
      orgLogoURL:
        "https://salt.tkbcdn.com/ts/ds/10/6b/83/c08a7f5373611aee68e51c9d10a643d9.jpg",
      orgName: "Những Thành Phố Mơ Màng",
      orgDescription: "Những Thành Phố Mơ Màng",
      created_at: "2024-06-22 06:41:35",
      updated_at: "2024-06-22 08:17:16",
    },
  ],
};

const EventDetail = () => {
  const { id } = useParams();

  const [organizationlogin, setOrganizationlogin] = useState(false);

  const checkIfOrganizationIsLoggedIn = () => {
    const organization = localStorage.getItem("Organizationuser");
    console.log("checkorganization", organization);
    if (organization) {
      setOrganizationlogin(organization);
      return true;
    }
    return false;
  };

  useEffect(() => {
    const Organizationloggedin = checkIfOrganizationIsLoggedIn();
    setOrganizationlogin(Organizationloggedin);
  })

  const checkIfUserIsLoggedIn = () => {
    const user = localStorage.getItem("user");
    if (user) {
      return true;
    }
    return false;
  };

  // useEffect(() => {
  //   if (!checkIfUserIsLoggedIn()) {
  //     window.location.href = `/SignIn`;
  //   }
  // }, []);

  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/buyticket/${id}`);
  };

  return (
    <div className="lg:pt-36 m-auto flex flex-col bg-white justify-center items-center">
      <div className="w-3/4 bg-white">
        <div className={`${styles.meinho}`}>
          <p>
            <span className={styles.destaque}>{data.Events[0].name}</span>
          </p>
        </div>
        <div className="grid grid-cols-2 mt-4 gap-[700px]">
          <button
            type="button"
            className="sm:min-w-[330px] min-w-[100px] px-4 py-2.5 border bg-transparent text-primary-500 text-xl font-semibold rounded shadow-md cursor-default"
          >
            From: {data.Events[0].minTicketPrice}₫
          </button>
          {organizationlogin ? (
            <button
              type="button"
              onClick={() => (window.location.href = "/handleTicket")}
              className="sm:min-w-[330px] min-w-[180px] px-4 py-3 bg-primary-500 hover:bg-primary-700 text-white text-xl font-semibold rounded shadow-lg shadow-primary-500/50"
              // onClick={handleBuyNow}
            >
              Manage Ticket
            </button>
          ) : (
            <button
              type="button"
              onClick={handleCardClick}
              className="sm:min-w-[330px] min-w-[180px] px-4 py-3 bg-primary-500 hover:bg-primary-700 text-white text-xl font-semibold rounded shadow-lg shadow-primary-500/50"
              // onClick={handleBuyNow}
            >
              Buy now
            </button>
          )}
        </div>
        <img
          src={
            "https://salt.tkbcdn.com/ts/ds/9f/0b/d4/f19a8a171d730418077d310ff82e7224.jpg"
          }
          alt={name}
          className="object-cover object-center w-full h-full sm:rounded-lg mt-12"
        />
        <div className="w-full mx-8 grid items-start grid-cols-1 lg:grid-cols-9 gap-12">
          <div className="lg:col-span-5 ml-8">
            <h2 className="text-2xl font-semibold text-gray-700">
              {data.Events?.name}
            </h2>
          </div>
        </div>
      </div>

      <div className="w-3/4 p-6 mt-8 bg-gray-100">
        <div className={`${styles.meinho}`}>
          <p>
            <span className={styles.destaque}>Description</span>
          </p>
        </div>
        <div
          className="p-8"
          dangerouslySetInnerHTML={{
            __html: data.Events[0].description,
          }}
        />
      </div>

      <div className="w-3/4 p-6 my-8 bg-gray-100">
        <div className={`${styles.meinho}`}>
          <p className="mb-8">
            <span className={styles.destaque}>Tickets</span>
          </p>
        </div>
      </div>
    </div>
  );
};

export default EventDetail;
