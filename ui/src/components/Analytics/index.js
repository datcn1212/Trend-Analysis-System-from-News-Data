import React, { useEffect } from "react";
import * as S from "./styles";
import Search from "../../assets/icons/search-small.png";
import Arrow from "../../assets/icons/arrow-down-b.png";
import Button from "../UI/Button";
import Graph from "../UI/Graph";
import Time from "../UI/Time";
import LineChart from "../LineChart";
import BarChart from "../BarChart";
import { useState } from "react";

import CountTopicStore from "./countTopicStore";
import AllKeywordsStore from "./allKeywordsStore";

export default function Analytics() {

  const countTopics = CountTopicStore;
  let [countTopic, setCountTopic] = useState([{ x: 1, y: 1 }]);
  useEffect(() => {
    const fetchDataTopic = async () => {
      countTopic = await countTopics.fetchCountTopic("20230601", "20230602");
      setCountTopic(countTopic);
    };
    fetchDataTopic();
  }, []);


  const allKeywords = AllKeywordsStore;
  let [allKeyword, setAllKeywords] = useState([{ x: 1, y: 1 }]);
  useEffect(() => {
    const fetchDataKw = async () => {
      allKeyword = await allKeywords.fetchAllKeywords("20230601", "20230602");
      setAllKeywords(allKeyword);
    };
    fetchDataKw();
  }, []);



  const graphData = [
    {
      title: "Average response Time",
      percentage: "+4.14%",
      color: "#F05D23",
      others: [
        {
          title: "Average Response Time",
          time: "30 Mins",
        },
        {
          title: "Response Time",
          time: "1 Hour 30 Mins",
        },
      ],
      graph: countTopic,
    },
    {
      title: "Replies per resolution",
      percentage: "+4.14%",
      color: "#3E68FF",
      others: [
        {
          title: "Average Replies",
          time: "30 Mins",
        },
        {
          title: "Response Time",
          time: "1 Hour 30 Mins",
        },
      ],
      graph: countTopic,
    },
    {
      title: "Average resolution time",
      percentage: "+4.14%",
      color: "#FB6491",
      others: [
        {
          title: "Average Resolution Rate",
          time: "30 Mins",
        },
        {
          title: "Response Time",
          time: "1 Hour 30 Mins",
        },
      ],
      graph: countTopic,
    },
    {
      title: "First contact resolution rate",
      percentage: "+4.14%",
      color: "#07C9E2",
      others: [
        {
          title: "Average Contact Rate",
          time: "30 Mins",
        },
        {
          title: "Response Time",
          time: "1 Hour 30 Mins",
        },
      ],
      graph: countTopic,
    },
  ];

  return (
    <S.Container>
      <S.Top>
        <h2>Analytics</h2>
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
      {graphData.map((data, i) => (
        <S.Analytics key={i}>
          <Graph
            graphHeader={data.title}
            percentage={data.percentage}
            priority={data.color}
          >
            <BarChart
              defaultColors={[data.color]}
              title={data.title}
              graph={data.graph}
            />
          </Graph>
          <S.TimeWrap>
            {data.others.map((item, index) => (
              <Time title={item.title} time={item.time} key={`time ${index}`} />
            ))}

            {/* <Time title="Response Time" time="1 Hour 30 Mins" /> */}
          </S.TimeWrap>
        </S.Analytics>
      ))}
    </S.Container>
  );
}
