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
import ReactWordcloud from 'react-wordcloud';

import CountTopicStore from "./kwStore";
// import AllKeywordsStore from "./allKeywordsStore";


export default function Keyword() {
  const countTopics = CountTopicStore;
  let [countTopic, setCountTopic] = useState([{"a": 1}]);

  useEffect(() => {
    const fetchDataTopic = async () => {
      countTopic = await countTopics.fetchCountTopic('thoi_su','20230624','20230624');
      console.log(countTopic);
      setCountTopic(countTopic);
    };
    fetchDataTopic();
  }, []);

  const callbacks = {
    getWordColor: word => word.value > 50 ? "blue" : "red",
    onWordClick: console.log,
    onWordMouseOver: console.log,
    getWordTooltip: word => `${word.text} (${word.value}) [${word.value > 50 ? "good" : "bad"}]`,
  }
  const options = {
    rotations: 3,
    rotationAngles: [0, 0],
  };
  const size = [600, 400];
  const words = [
    {
      text: 'told',
      value: 64,
    },
    {
      text: 'mistake',
      value: 11,
    },
    {
      text: 'thought',
      value: 16,
    },
    {
      text: 'bad',
      value: 17,
    },
  ];
   
  const result = countTopic.reduce((acc, currentValue) => {
    const existingItem = acc.find(item => item.text === currentValue);
    if (existingItem) {
      existingItem.value++;
    } else {
      acc.push({ text: currentValue, value: 1 });
    }
    return acc;
  }, []);

  function MyWordcloud() {
    return (
      <ReactWordcloud
        callbacks={callbacks}
        options={options}
        size={size}
        words={result}
      />
    );
  }

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
      
        <S.Analytics>
          
          <MyWordcloud/>

        </S.Analytics>
     
    </S.Container>
  );
}
