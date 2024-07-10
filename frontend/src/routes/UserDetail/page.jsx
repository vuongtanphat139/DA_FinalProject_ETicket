import React from "react";
import styles from "../Events/Event.module.css";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { Tabs } from 'antd';
import Profile from "./profile";
import UserEvent from "./user-event";

const theme = createTheme();

const onChange = (key) => {
  console.log(key);
};

const items = [
  {
    key: '1',
    label: 'Profile',
    children: <Profile></Profile>,
  },
  {
    key: '2',
    label: 'Your Events',
    children: <UserEvent></UserEvent>,
  },
];

const UserDetail = () => {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <ThemeProvider theme={theme}>
      <div className={`${styles.meinho} pt-16`}>
        <p>
          <span className={styles.destaque}>User Detail</span>
        </p>
      </div>
      <div className="w-full">
      <Tabs defaultActiveKey="1" items={items} onChange={onChange} size={"large"} className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8"/>;
      </div>
    </ThemeProvider>
  );
};

export default UserDetail;
