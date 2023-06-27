import React from "react";
import * as S from "./styles";
import { Chart } from "react-charts";

export default function LineChart({ defaultColors,title,graph }) {
  const data = [
    {
      label: title,
      data: graph
    },
  ];

  const primaryAxis = React.useMemo(
    () => ({
      getValue: (value) => value.x,
    }),
    []
  );

  const secondaryAxes = React.useMemo(
    () => [
      {
        getValue: (value) => value.y,
        elementType: "line",
      },
    ],
    []
  );

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
