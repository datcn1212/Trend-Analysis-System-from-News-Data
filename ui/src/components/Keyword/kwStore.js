import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../service/common";

class CountTopicStore {
  isLoading = false;
  graph = [];


  async fetchCountTopic(topic, startTime, endTime) {
    
    const res = await APIS.getTopicKeywords(topic, startTime, endTime);
    return Object.entries(res.data).map(([x, y]) => (y));
  }
}

export default new CountTopicStore();
