import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../service/common";

class CountTopicStore {
  async fetchCountTopic(topic, startTime, endTime) {
    const res = await APIS.getTopicKeywords(topic, startTime, endTime);
    return res.data.data;
  }

  async fetchSearchData(word) {
    const res = await APIS.getSearchData(word);
    console.log(res.data.data);
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
}

export default new CountTopicStore();
