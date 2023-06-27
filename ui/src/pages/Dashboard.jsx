import React from "react";
import Analytics from "../components/Analytics";
import SearchES from "../components/SearchES";
import Keyword from "../components/Keyword";
import NavBar from "../components/NavBar";
import Tab from "../components/Tab";
import TopBar from "../components/TopBar";
import * as S from "./styles";
import { routingPaths } from "../route/routing";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function Analytic() {
  return (
    <S.Container>
      <NavBar />
      <S.Main>
        <Analytics />
      </S.Main>
    </S.Container>
  );
}

function KeyworD() {
  return (
    <S.Container>
      <NavBar />
      <S.Main>
        <Keyword />
      </S.Main>
    </S.Container>
  );
}

function SSearch() {
  return (
    <S.Container>
      <NavBar />
      <S.Main>
        <SearchES />
      </S.Main>
    </S.Container>
  );
}


export default function Dashboard() {
  return (
    <BrowserRouter>
    <Routes>
      <Route exact path={routingPaths.overview} element = {<Analytic/>}/>
      <Route path={routingPaths.keyword} element = {<KeyworD/>}/>
      <Route path={routingPaths.search} element = {<SSearch/>}/>
    </Routes>
    </BrowserRouter>
  );
}

export function Search() {
  return (
    <S.Container>
      <NavBar />
      <S.Main>
        {/* <header>
          <TopBar />
          <Tab />
        </header> */}
        <SearchES />
      </S.Main>
    </S.Container>
  );
}


<S.Container>
          <NavBar />
          <S.Main>
            {/* <header>
          <TopBar />
          <Tab />
        </header> */}
            <Analytics />
          </S.Main>
        </S.Container>