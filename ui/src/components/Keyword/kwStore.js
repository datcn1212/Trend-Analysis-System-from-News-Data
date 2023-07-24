import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../service/common";

function convertDate(originalDate) {
  const year = originalDate.substring(0, 4);
  const month = originalDate.substring(4, 6);
  const day = originalDate.substring(6, 8);

  const formattedDate = `${day}/${month}/${year}`;
  return formattedDate;
}

function sortByFrequency(arr) {
  const frequencyMap = arr.reduce((map, word) => {
    map[word] = (map[word] || 0) + 1;
    return map;
  }, {});
  const uniqueWords = Array.from(new Set(arr));
  uniqueWords.sort((a, b) => frequencyMap[b] - frequencyMap[a]);
  return uniqueWords;
}

class CountTopicStore {

  async fetchCountTopic(topic, startTime, endTime) {
    const res = await APIS.getTopicKeywords(topic, startTime, endTime);
    console.log(sortByFrequency(res.data.data))
    return sortByFrequency(res.data.data);
  }

  async fetchSearchData(word) {
    const res = await APIS.getSearchData(word);

    if (res.data.data[0] == null) {
      return [
        {
          Author: 0,
          Href: 0,
          Title: 0,
        },
      ];
    }
    return res.data.data;
  }

  async fetchCountWordByTime(word, startTime, endTime) {
    const res = await APIS.getCountWordByTime(word, startTime, endTime);

    if (res.data.data[0] == null) {
      return [
        {
          x: "a",
          y: 0,
        },
      ];
    }

    return res.data.data.map((item) => ({
      x: convertDate(item.key),
      y: item.doc_count,
    }));
  }
}

export default new CountTopicStore();
