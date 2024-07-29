import React, { useEffect } from "react";
import dynamic from "next/dynamic";
import { Column, Paging, Pager } from "devextreme-react/data-grid";
import { LuMoreHorizontal } from "react-icons/lu";
import CmtDropdownMenu from "@/assets/DropdownMenu";
import { AiFillDelete } from "react-icons/ai";
import { BiEdit } from "react-icons/bi";
import EditDoctorDetailsModal from "./edit-doctor-details-modal";
import DeleteDoctorModal from "./delete-doctor-modal";
import { getAllDoctors } from "@/redux/features/doctors";
import { useSelector, useDispatch } from "react-redux";
import { useAuth } from "@/assets/hooks/use-auth";

const DataGrid = dynamic(() => import("devextreme-react/data-grid"), {
  ssr: false,
});

const getActions = () => {
  let actions = [
    {
      action: "delete",
      label: "Delete",
      icon: <AiFillDelete className="text-warning text-xl mx-2" />,
    },
    {
      action: "edit",
      label: "Edit",
      icon: <BiEdit className="text-xl text-success  mx-2" />,
    },
  ];

  return actions;
};

const AdminDoctorsDataGrid = () => {
  const [searchQuery, setSearchQuery] = React.useState("");
  const userActions = getActions();
  const [open, setOpen] = React.useState(false);
  const [deleteOpen, setDeleteOpen] = React.useState(false);
  const [selectedRowData, setSelectedRowData] = React.useState({});
  const dispatch = useDispatch();
  const { doctors } = useSelector((store) => store.doctor);
  const authUser = useAuth();

  console.log("AUTH_USER ",authUser);

  useEffect(() => {
    if (authUser) {
      dispatch(getAllDoctors(authUser));
    }
  }, []);

  const onMenuClick = async (menu, data) => {
    if (menu.action === "delete") {
      setSelectedRowData(data);
      setDeleteOpen(true);
    } else if (menu.action === "edit") {
      setSelectedRowData(data);
      setOpen(true);
    }
  };

  const actionsFunc = ({ data }) => {
    return (
      <>
        <CmtDropdownMenu
          sx={{ cursor: "pointer" }}
          items={userActions}
          onItemClick={(menu) => onMenuClick(menu, data)}
          TriggerComponent={
            <LuMoreHorizontal className="cursor-pointer text-xl" />
          }
        />
      </>
    );
  };

  return (
    <section>
      <DataGrid
        dataSource={doctors}
        allowColumnReordering={true}
        rowAlternationEnabled={true}
        showBorders={true}
        remoteOperations={true}
        showColumnLines={true}
        showRowLines={true}
        wordWrapEnabled={true}
        allowPaging={true}
        className="shadow-xl w-full"
        height={"70vh"}
      >
        <Pager
          visible={true}
          // allowedPageSizes={allowedPageSizes}
          showPageSizeSelector={true}
          showNavigationButtons={true}
        />
        <Column
          dataField="first_name"
          caption="First Name"
          width={200}
          allowFiltering={true}
          allowSearch={true}
        />
        <Column
          dataField="last_name"
          caption="Last Name"
          width={200}
          allowFiltering={true}
          allowSearch={true}
        />
        <Column dataField="email" caption="Email" width={140} />
        <Column dataField="role" caption="Role" width={200} />
      </DataGrid>
      <EditDoctorDetailsModal {...{ open, setOpen, selectedRowData }} />
      <DeleteDoctorModal {...{ deleteOpen, setDeleteOpen, selectedRowData }} />
    </section>
  );
};

export default AdminDoctorsDataGrid;
