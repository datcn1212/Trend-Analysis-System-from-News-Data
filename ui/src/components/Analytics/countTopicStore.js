import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../service/common";

class CountTopicStore {
  isLoading = false;
  graph = [];

  // constructor() {
  //   makeObservable(this, {
  //     isLoading: observable,
  //     graph: observable,
  //     fetchCountTopic: action,
  //   });
  // }

  async fetchCountTopic(startTime, endTime) {
    const res = await APIS.getCountTopic(startTime, endTime)
    return Object.entries(res.data).map(([x, y]) => ({ x, y }));
  }
}

export default new CountTopicStore();
