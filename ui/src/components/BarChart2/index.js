import React from "react";
import * as S from "./styles";
import { Chart } from "react-charts";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const labels = [
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
  "Số hóa",
];

export default function BarChart2({ defaultColors, title, graph }) {
  const data = {
    labels,
    datasets: [
      {
        label: "number of articles",
        data: labels.map((la) => {
          for (let i = 0; i < graph.length; i++) {
            if (graph[i].x === la) return graph[i].y;
          }
          return 0;
        }),
        backgroundColor: defaultColors,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: false,
      },
    },
    borderWidth: "1000px"
  };

  return (
    <S.Container>
      <Bar options={options} data={data} />
    </S.Container>
  );
}
