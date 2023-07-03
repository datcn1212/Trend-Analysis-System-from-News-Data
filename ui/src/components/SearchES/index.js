import React, { useEffect } from "react";
import * as S from "./styles";
import Search from "../../assets/icons/search-small.png";
import Arrow from "../../assets/icons/arrow-down-b.png";
import Button from "../UI/Button";
import Graph from "../UI/Graph";
import Time from "../UI/Time";
import LineChart from "../LineChart";
import BarChart from "../BarChart";
import BarChart2 from "../BarChart2";
import { useState } from "react";
import ReactWordcloud from "react-wordcloud";
import Dropdown from "react-dropdown";
import "react-dropdown/style.css";
import CountTopicStore from "./searchStore";
// import AllKeywordsStore from "./allKeywordsStore";

export default function SearchES() {
  let [word, setWord] = useState("Việt Nam");
  let [searchData, setSearchData] = useState([
    {
      Href: "",
      Title: "<Choose one of above words>",
    },
  ]);
  const handleWord = (string) => {
    setWord(string.target.value);
  };
  const handleSearch = () => {
    fetchSearchData();
  };
  const fetchSearchData = async () => {
    const countTopics = CountTopicStore;
    const searchData = await countTopics.fetchSearchData(word);
    setSearchData(searchData);
  };

  useEffect(() => {
    fetchSearchData();
  }, []);

  return (
    <S.Container>
      <S.Top>
        <h2>Articles Search</h2>
        <S.Right>
          <S.Line />
          <Button background="#25BB87" width="105px">
            Export
          </Button>
        </S.Right>
      </S.Top>
      <br></br>
      <S.Wrap>
        <div>
          <h3>Input :</h3>
        </div>
        &nbsp;&nbsp;&nbsp;
        <S.InputField>
          <S.SearchImg src={Search} />
          <S.Input
            type="text"
            placeholder="Search"
            value={word}
            onChange={handleWord}
          />
        </S.InputField>
        <S.button onClick={handleSearch}>Search</S.button>
      </S.Wrap>
      <br></br>
      <br></br>
      <h3>Suggested Articles:</h3>
      <br></br>
      <div>
        <p>
          {searchData.map((item, index) => {
            return (
              <div>
                <p>
                  {index + 1}. {item["Title"]}
                </p>
                <a href={item["Href"]} target="_blank">
                  {item["Href"]}
                </a>
              </div>
            );
          })}
        </p>
      </div>
    </S.Container>
  );
}
