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

import CountTopicStore from "./countTopicStore";
import AllKeywordsStore from "./allKeywordsStore";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

function getSumArticle(countTopic) {
  let sum = 0;
  for (let i = 0; i < countTopic.length; i++) {
    sum += countTopic[i].y;
  }
  return sum;
}
function convertDateToString(date) {
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");

  const formattedDate = `${year}${month}${day}`;

  return formattedDate;
}

export default function Analytics() {
  const [startDate, setStartDate] = useState(new Date(2023, 5, 24));
  const [endDate, setEndDate] = useState(new Date(2023, 5, 24));

  const handleStartDateChange = (date) => {
    setStartDate(date);
  };
  const handleEndDateChange = (date) => {
    setEndDate(date);
  };
  const handleApplyChanges = () => {
    fetchData();
    console.log("Start Date:", startDate);
    console.log("End Date:", endDate);
  };
  const fetchData = async () => {
    const countTopics = CountTopicStore;
    const countTopic = await countTopics.fetchCountTopic(
      convertDateToString(startDate),
      convertDateToString(endDate)
    );
    setCountTopic(countTopic);

    const allKeywords = AllKeywordsStore;
    const allKeyword = await allKeywords.fetchAllKeywords(
      convertDateToString(startDate),
      convertDateToString(endDate)
    );
    setAllKeywords(allKeyword);
  };

  const countTopics = CountTopicStore;
  let [countTopic, setCountTopic] = useState([{ x: 1, y: 1 }]);
  useEffect(() => {
    fetchData();
  }, []);

  const allKeywords = AllKeywordsStore;
  let [allKeyword, setAllKeywords] = useState([{ x: 1, y: 1 }]);
  useEffect(() => {
    fetchData();
  }, []);

  const graphData = [
    {
      title: "Number of articles per Topic",
      percentage: "+4.14%",
      color: "#F05D23",
      others: [
        {
          title: "Total number",
          time: getSumArticle(countTopic) + " articles",
        },
        {
          title: "Average number per Topic",
          time: (getSumArticle(countTopic) / 13).toFixed(1) + " articles",
        },
      ],
      graph: countTopic,
    },
  ];

  return (
    <S.Container>
      <S.Top>
        <h2>Overview</h2>
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
          <S.Container1>
            <S.Top1>
              <S.Wrap>
                <h6>{data.title}</h6>
                {/* <S.Percentage className="text-sm">{data.percentage}</S.Percentage> */}
              </S.Wrap>
              <S.Wrap>
                <S.Calender>
                  {/* <span className="text-sm">This Month</span>
                  <img src={Calendar} alt="calender"/> */}
                  {/* <div> */}
                  <div>
                    <label>Start Date:</label>
                    <DatePicker
                      selected={startDate}
                      onChange={handleStartDateChange}
                    />
                  </div>
                  <div>
                    <label>End Date:</label>
                    <DatePicker
                      selected={endDate}
                      onChange={handleEndDateChange}
                    />
                  </div>
                  <S.ApplyButton onClick={handleApplyChanges}>
                    Submit
                  </S.ApplyButton>
                  {/* </div> */}
                </S.Calender>
              </S.Wrap>
            </S.Top1>
            <BarChart
              defaultColors={[data.color]}
              title={data.title}
              graph={data.graph}
            />
          </S.Container1>

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
