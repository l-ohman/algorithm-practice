// ** Deprecated, now using `table.py` in root dir
const stats = require("../stats.json");

function restructureData(stats) {
  const defaultStruct = {
    easy: 0,
    medium: 0,
    hard: 0,
  };
  const tableData = {
    totals: { ...defaultStruct },
  };
  let languageTotals = {
    javascript: 0,
    python: 0,
    both: 0,
  };

  for (let i = 0; i < stats.length; i++) {
    if (stats[i].title === "") continue;
    if (stats[i].type.slice(0, 6) === "Binary") stats[i].type = "Binary Tree";
    if (!tableData[stats[i].type]) {
      tableData[stats[i].type] = { ...defaultStruct };
    }

    tableData[stats[i].type][stats[i].difficulty] += 1;
    tableData.totals[stats[i].difficulty] += 1;

    if (stats[i].javascript && stats[i].python) {
      languageTotals.both += 1;
    }
    if (stats[i].javascript) {
      languageTotals.javascript += 1;
    }
    if (stats[i].python) {
      languageTotals.python += 1;
    }
  }
  console.log("<!--", languageTotals, "-->");
  return tableData;
}

function convertDataToTable(data) {
  console.log("| |Easy|Medium|Hard|Total|\n|-|-|-|-|-|");

  const keys = Object.keys(data).sort();
  let totals;
  for (let i = 0; i < keys.length; i++) {
    const type = keys[i];
    if (type === "totals") {
      totals = data[type];
    } else {
      console.log(
        `|${type}|${data[type].easy}|${data[type].medium}|${data[type].hard}|${
          data[type].easy + data[type].medium + data[type].hard
        }|`
      );
    }
  }
  console.log(
    `|Totals|**${data.totals.easy}**|**${data.totals.medium}**|**${
      data.totals.hard
    }**|**${data.totals.easy + data.totals.medium + data.totals.hard}**|`
  );
}

if (require.main === module) {
  convertDataToTable(restructureData(stats));
}
