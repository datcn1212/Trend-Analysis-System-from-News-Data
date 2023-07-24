import styled from "styled-components";
export const Container = styled.main`
  padding: 0 40px;
`;
export const Top = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 32px 0;
`;
export const a = styled.a`
  color: teal;
  font-weight: bold;
  `;
  export const a2 = styled.a`
  color: blue;
  font-weight: bold;
  `;
export const p = styled.p`
color: black;
`;

export const Right = styled.div`
  display: flex;
  align-items: center;
`;
export const InputField = styled.div`
  position: relative;
  width: 350px;
  padding-right: 24px;
`;
export const SearchImg = styled.img`
  position: absolute;
  top: 14px;
  left: 0;
  padding-left: 16px;
`;
export const Input = styled.input`
  background: transaparent;
  border-radius: 10px;
  border: 1px solid #e1e1eb;
  padding: 12px 16px 12px 53px;
  width: 100%;
  height: 44px;
`;
export const Filter = styled.div`
  background: transaparent;
  border-radius: 10px;
  border: 1px solid #e1e1eb;
  padding: 16px;
  width: 160px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;
export const FilterImg = styled.img`
  padding-left: 16px;
`;
export const Line = styled.div`
  width: 1px;
  background: #e1e1eb;
  height: 1px;
  padding: 0 16px;
  transform: rotate(90deg);
`;
export const NotificationWrap = styled.div`
  border-right: 1px solid #e1e1eb;
  padding-right: 16px;
  display: flex;
  align-items: center;
`;
export const Notification = styled.span`
  width: 16px;
  height: 16px;
  background: #f25a68;
  border-radius: 4px;
  color: white;
  margin: 0 8px 0 4px;
  display: flex;
  align-items: center;
  justify-content: center;
`;
export const ProfileWrap = styled.div`
  display: flex;
  align-items: center;
  padding-left: 16px;
`;
export const Profile = styled.span`
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: block;
  border: 1px solid #6837ef;
  margin-right: 8px;
`;
export const Analytics = styled.div`
  display: flex;
  border: 0px solid #ecebf5;
  border-radius: 10px;
  height: 150px;
  margin-bottom: 10px;
  :last-child {
    margin-bottom: 0;
  }
`;
export const TimeWrap = styled.div`
  padding: 26px 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
`;

export const Container1 = styled.div`
  width: 100%;
  border-right: 1px solid #ecebf5;
  padding: 26px 24px;
  font-weight: 500;
`;
export const Top1 = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;
export const Wrap = styled.div`
  display: flex;
  align-items: center;
`;
export const Percentage = styled.span`
  padding: 4px 12px;
  color: #25bb87;
  background: rgba(37, 187, 135, 0.1);
  margin-left: 16px;
  border-radius: 4px;
`;
export const PriorityWrap = styled.div`
  border-right: 1px solid #e1e1eb;
  padding-right: 16px;
  display: flex;
  align-items: center;
`;
export const Priority = styled.span`
  width: 10px;
  height: 10px;

  border-radius: 2px;
  display: block;
  margin-right: 8px;
  background: ${(props) => (props.priority ? props.priority : "#f05d23")};
`;
export const Calender = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  width: 560px;
  border: 1px solid #e1e1eb;
  border-radius: 8px;
  margin-left: 16px;
`;
export const ApplyButton = styled.button`
  background-color: #25bb87;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
`;

export const button = styled.button`
  background-color: #e0eef9;
  color: black;
  border: none;
  padding: 6px 10px;
  border-radius: 10px;
  cursor: pointer;
`;

export const TextWindow = styled.div`
margin-top: 10px;
padding: 10px;
background-color: #f0f0f0;
border: 1px solid #ccc;
border-radius: 5px;
`;
export const ButtonContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
`;

export const Button = styled.button`
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
`;

export const WindowContainer = styled.div`
  position: fixed;
  top: 40%;
  left: 84%;
  transform: translate(-50%, -50%);
  background-color: #F2E0FA;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  width: 400px;
  height: 450px;
  z-index: 999;
  overflow: auto; 
`;

export const CloseButton = styled.button`
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
`;

export const button2 = styled.button`
  background-color: #E0F9EE;
  color: red;
  border: none;
  padding: 5px 7px;
  border-radius: 15px;
  cursor: pointer;
`;