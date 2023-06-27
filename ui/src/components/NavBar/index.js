import React from "react";
import * as S from "./styles";
import Calendar from "../../assets/icons/calendar-nav.png";
import Message from "../../assets/icons/message.png";
import Time from "../../assets/icons/time.png";
import User from "../../assets/icons/user.png";
import Shape from "../../assets/icons/shape.png";
import Bell from "../../assets/icons/bell.png";
import Arrow from "../../assets/icons/arrow-right.png";
import ArrowDown from "../../assets/icons/arrow-down-nav.png";
import Search from "../../assets/icons/search.png";

export default function NavBar() {
  return (
    <S.Wrapper>
      <S.Container>
        <S.Profile>
          {/* <S.ProfileImg></S.ProfileImg> */}
          <S.ProfileInfo>
            News Trending Analytics
            <S.Email className="text-sm">canada2k1@gmail.com</S.Email>
          </S.ProfileInfo>
        </S.Profile>
        <S.List>
          <S.ListItem className="dropdown">
            <S.Item href="/" className="active">
              <S.ItemIcon src={Shape} alt="user" />
              Overview
            </S.Item>
          </S.ListItem>

          <S.ListItem className="dropdown">
            <S.Item href="keyword" className="active">
              <S.ItemIcon src={Bell} alt="message" />
              Keyword Analysis
            </S.Item>
          </S.ListItem>

          <S.ListItem className="dropdown">
            <S.Item href="search" className="active">
              <S.ItemIcon src={Search} alt="search" />
              Articles Search
            </S.Item>
          </S.ListItem>
        </S.List>
      </S.Container>
    </S.Wrapper>
  );
}
