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

  // Create an array of states to handle visibility for each item
  const [isTextVisibleArray, setIsTextVisibleArray] = useState([]);

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

    // Initialize isTextVisibleArray with false for each item in searchData
    setIsTextVisibleArray(Array(searchData.length).fill(false));
  };

  // Function to handle the "Detail" button click for a specific item
  const handleButtonClick = (index) => {
    const updatedIsTextVisibleArray = [...isTextVisibleArray];
    updatedIsTextVisibleArray[index] = !updatedIsTextVisibleArray[index];
    setIsTextVisibleArray(updatedIsTextVisibleArray);
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
              <div key={index}>
                <S.p>
                  {index + 1}. {item["Title"]} &nbsp;&nbsp;&nbsp;
                  <a>
                    <S.button2 onClick={() => handleButtonClick(index)}>
                      Detail
                    </S.button2>
                    {isTextVisibleArray[index] && (
                      <S.WindowContainer>
                        <S.CloseButton onClick={() => handleButtonClick(index)}>
                          Close
                        </S.CloseButton>
                        <br></br>
                        <p>
                          <S.a2>Nội dung bài báo: {item["Title"]}</S.a2>
                          <br />
                          {item["Date"]}<br></br> <br></br>
                          {/* {item["Description"]} */}
                          {item["Body"]}
                        </p>
                      </S.WindowContainer>
                    )}
                  </a>
                </S.p>

                <a href={item["Href"]} target="_blank">
                  {item["Href"]}
                </a>
                <p>
                  Từ khóa:{" "}
                  {item["keyword_lst"]?.map((keyword, keywordIndex) => {
                    return (
                      <S.a key={keywordIndex}>{keyword.replace(/_/g, " ")}; </S.a>
                    );
                  })}
                </p>
                <br />
              </div>
            );
          })}
        </p>
      </div>
    </S.Container>
  );
}
