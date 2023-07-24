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
import CountTopicStore from "./kwStore";

const dict = {
  "Đời sống": "doi_song",
  "Du lịch": "du_lich",
  "Giải trí": "giai_tri",
  "Giáo dục": "giao_duc",
  "Khoa học": "khoa_hoc",
  "Kinh doanh": "kinh_doanh",
  "Pháp luật": "phap_luat",
  "Sức khỏe": "suc_khoe",
  "Thế giới": "the_gioi",
  "Thể thao": "the_thao",
  "Thời sự": "thoi_su",
  "Bất động sản": "bat_dong_san",
  "Số hóa": "so-hoa",
};

function convertDateToString(date) {
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");

  const formattedDate = `${year}${month}${day}`;

  return formattedDate;
}

export default function Keyword() {
  let [countTopic, setCountTopic] = useState(["dat"]);
  let [Topic, setTopic] = useState("thoi_su");
  let [startDate, setStartDate] = useState("20230706");
  let [word, setWord] = useState("Việt Nam");
  let [searchData, setSearchData] = useState([
    {
      Href: "",
      Title: "<Choose one of above words>",
    },
  ]);

  let [wordByTime, setWordByTime] = useState([
    {
      x: "a",
      y: 1,
    },
  ]);


  const handleWord = (string) => {
    setWord(string);
    fetSearchData();
  };

  const handleTopic = (string1) => {
    const string = string1.value;
    setTopic(dict[string]);
  };

  const submit = () => {
    fetchDataTopic();
  };

  const handleStartDateChange = (string1) => {
    const string = string1.value;
    const currentDate = new Date();
    if (string == "1 day ago") {
      const _1DaysAgo = new Date(currentDate);
      _1DaysAgo.setDate(currentDate.getDate() - 1);
      setStartDate(convertDateToString(_1DaysAgo));
    } else if (string == "3 days ago") {
      const _3DaysAgo = new Date(currentDate);
      _3DaysAgo.setDate(currentDate.getDate() - 3);
      setStartDate(convertDateToString(_3DaysAgo));
    } else if (string == "1 week ago") {
      const _7DaysAgo = new Date(currentDate);
      _7DaysAgo.setDate(currentDate.getDate() - 7);
      setStartDate(convertDateToString(_7DaysAgo));
    } else {
      const _30DaysAgo = new Date(currentDate);
      _30DaysAgo.setDate(currentDate.getDate() - 30);
      setStartDate(convertDateToString(_30DaysAgo));
    }
  };

  const fetchDataTopic = async () => {
    const countTopics = CountTopicStore;
    const countTopic = await countTopics.fetchCountTopic(
      Topic,
      startDate,
      '20230707'
    );
    setCountTopic(countTopic);
  };

  const fetSearchData = async () => {
    const countTopics = CountTopicStore;
    const searchData = await countTopics.fetchSearchData(word);
    setSearchData(searchData);
    const wordData = await countTopics.fetchCountWordByTime(word);
    setWordByTime(wordData);
  };

  useEffect(() => {
    fetchDataTopic();
  }, []);

  // const callbacks = {
  //   getWordColor: word => word.value > 50 ? "blue" : "red",
  //   onWordClick: console.log,
  //   onWordMouseOver: console.log,
  //   getWordTooltip: word => `${word.text} (${word.value}) [${word.value > 50 ? "good" : "bad"}]`,
  // }
  // const options = {
  //   rotations: 3,
  //   rotationAngles: [0, 0],
  // };
  // const size = [600, 400];
  // const words = [
  //   {
  //     text: 'told',
  //     value: 64,
  //   },
  //   {
  //     text: 'mistake',
  //     value: 11,
  //   },
  //   {
  //     text: 'thought',
  //     value: 16,
  //   },
  //   {
  //     text: 'bad',
  //     value: 17,
  //   },
  // ];

  // const result = countTopic.reduce((acc, currentValue) => {
  //   const existingItem = acc.find(item => item.text === currentValue);
  //   if (existingItem) {
  //     existingItem.value++;
  //   } else {
  //     acc.push({ text: currentValue, value: 1 });
  //   }
  //   return acc;
  // }, []);

  // function MyWordcloud() {
  //   return (
  //     <ReactWordcloud
  //       callbacks={callbacks}
  //       options={options}
  //       size={size}
  //       words={result}
  //     />
  //   );
  // }
  const word_data = {
    title: "Number of articles per Topic",
    color: "#F05D23",
    graph: wordByTime,
  };

  const options = [
    "Đời sống",
    "Du lịch",
    "Giải trí",
    "Giáo dục",
    "Khoa học",
    "Kinh doanh",
    "Pháp luật",
    "Sức khỏe",
    "Thế giới",
    "Thể thao",
    "Thời sự",
    "Bất động sản",
    "Số hóa"
  ];

  const options2 = ["1 day ago", "3 days ago", "1 week ago", "1 month ago"];

  const defaultOption = options[0];
  const defaultOption2 = options2[0];

  console.log(searchData);
  return (
    <S.Container>
      <S.Top>
        <h2>Keyword Analysis</h2>
        <S.Right>
          <S.InputField>
            <S.SearchImg src={Search} />
            <S.Input type="text" placeholder="Search" />
          </S.InputField>
          <S.Filter>
            <span>Filter Options</span>
            <S.FilterImg src={Arrow} />
          </S.Filter>
          <S.Line />
          <Button background="#25BB87" width="105px">
            Export
          </Button>
        </S.Right>
      </S.Top>
      <br></br>
      <S.Wrap>
        <div>
          <h3>Topic :</h3>
        </div>
        &nbsp;&nbsp;&nbsp;
        <div>
          <Dropdown
            options={options}
            onChange={handleTopic}
            value={defaultOption}
            placeholder="Select an option"
          />
        </div>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <div>
          <Dropdown
            options={options2}
            onChange={handleStartDateChange}
            value={defaultOption2}
            placeholder="Select an option"
          />
        </div>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <div>
          <S.ApplyButton onClick={submit}>Submit</S.ApplyButton>
        </div>
      </S.Wrap>
      <br></br>
      <S.Analytics>
        {/* <MyWordcloud/> */}

        <div>
          {countTopic.map((item, index) => {
            if (index < 25) {
              if (index % 9 == 0 && index != 0) {
                return (
                  <span>
                    <br></br>
                    <br></br>
                    <S.button key={index} onClick={() => handleWord(item)}>
                      {item}
                    </S.button>
                    &nbsp;&nbsp;&nbsp;
                  </span>
                );
              }
              return (
                <span>
                  <S.button key={index} onClick={() => handleWord(item)}>
                    {item}
                  </S.button>
                  &nbsp;&nbsp;&nbsp;
                </span>
              );
            }
          })}
          &nbsp;&nbsp;&nbsp;
        </div>
      </S.Analytics>
      <br></br>
      <h3>Suggested Articles for "{word}":</h3>
      <div>
        <p>
          {searchData.map((item, index) => {
            if(index < 5)
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
      <br></br>
      <h3>Variation of topic "{word}" over time:</h3>
      <S.Analytics>
      <BarChart
        defaultColors={[word_data.color]}
        title={word_data.title}
        graph={word_data.graph}
      />
      </S.Analytics>
    </S.Container>
  );
}
