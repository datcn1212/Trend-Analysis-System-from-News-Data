import { action, makeObservable, observable } from "mobx";
import _ from "lodash";
import APIS from "../../services/common";

class AllKeywordStore {
    curTrendingSymbols = [];
    symbolChartCellColor = [];
    latestTweets = [];
    isLoading = false;

    constructor() {
        makeObservable(this, {
            curTrendingSymbols: observable,
            symbolChartCellColor: observable,
            latestTweets: observable,
            isLoading: observable,
            fetchOverviewInfo: action,
        });
    }

    fetchAllKeywords() {
        this.isLoading = true;
        APIS.getAllKeywords().then((res) => {
            this.curTrendingSymbols = _.map(res.data.symbols, (symbol) => ({
                "symbol": symbol.symbol.toUpperCase(),
                "tweet_count": symbol.tweet_count,
                "tweet_count_positive": symbol.tweet_count_positive,
                "tweet_count_negative": symbol.tweet_count_negative,
            }));
            this.symbolChartCellColor = _.map(
                res.data.symbols,
                (symbol) => symbol.color
            );
            this.latestTweets = res.data.tweets;
            this.isLoading = false;
        });
    }
}

export default new AnalyticsStore();
