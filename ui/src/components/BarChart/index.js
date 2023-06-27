import React from "react";
import * as S from "./styles";
import { Chart } from "react-charts";

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

export default function BarChart({ defaultColors,title,graph }) {
  const data = [
    {
      label: title,
      data: graph
    },
  ];

  const primaryAxis = React.useMemo(
    () => ({
      getValue: (value) => value.x
    }),
    []
  );

  const secondaryAxes = React.useMemo(
    () => [
      {
        getValue: (value) => value.y,
        suggestedMin: 0,
        elementType: "bar"
      },
    ],
    []
  );

  const options = {
    scales: {
      y: {
        type: "band", // Specify the scale type as "linear"
        suggestedMin: 0, // Dynamically calculate the suggestedMin
      },
    },
  };

  return (
    <S.Container>
      <Chart
        options={{
          options,
          data,
          primaryAxis,
          secondaryAxes,
          defaultColors,
        }}
      />
    </S.Container>
  );
}
