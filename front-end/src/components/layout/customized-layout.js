import React from "react";
import Sidebar from "./sidebar";
import CustomizedHeader from "./customized-header";


const CustomizedLayout = ({ children }) => {
  return (
    <div className="md:flex md:h-screen h-auto overflow-hidden bg-background">
      <div className="w-56 bg-white shadow-xl rounded md:block hidden">
        <Sidebar />
      </div>

      <div className="flex-1 overflow-y-auto hideMiddleSectionScrollbar">
        <CustomizedHeader />
        <div>{children}</div>
      </div>
    </div>
  );
};

export default CustomizedLayout;
