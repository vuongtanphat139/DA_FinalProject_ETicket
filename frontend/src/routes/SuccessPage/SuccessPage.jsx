import { Button, Result } from "antd";
import { useNavigate } from "react-router-dom";

const SuccessPage = () => {
  const navigate = useNavigate();

  const handleCardClick = () => {
    navigate(`/`);
  };
  return (
    <div className="h-[570px] flex items-center justify-center">
      <Result
        status="success"
        title="Successfully Purchased Ticket!"
        subTitle=""
        extra={[
          <Button onClick={handleCardClick} type="primary" key="console">
            Go back Home
          </Button>,
          //   <Button key="buy">Buy Again</Button>,
        ]}
      />
    </div>
  );
};

export default SuccessPage;