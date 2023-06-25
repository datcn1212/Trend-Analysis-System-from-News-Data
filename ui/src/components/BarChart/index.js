import React from "react";
import * as S from "./styles";
import { Chart } from "react-charts";

export default function BarChart({ defaultColors,title,graph }) {
  const data = [
    {
      label: title,
      data: graph
    },
  ];

  const axes = React.useMemo(
    () => [
      { primary: true, type: 'ordinal', position: 'left' },
      { position: 'bottom', type: 'linear', stacked: true }
    ],
    []
  );

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
        elementType: "bar"
      },
    ],
    []
  );

  const options = {
    scales: {
      y: {
        type: "linear", // Specify the scale type as "linear"
      },
    },
  };

  return (
    <S.Container>
      <Chart
        options={{
          data,
          primaryAxis,
          secondaryAxes,
          defaultColors,
        }}
      />
    </S.Container>
  );
}
