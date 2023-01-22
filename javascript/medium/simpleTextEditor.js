// medium,
// https://www.hackerrank.com/challenges/simple-text-editor/problem

class TextEditor {
  constructor(S = "") {
    this.text = S;
    this.previousStates = [];
  }
  append(W) {
    this.previousStates.push(this.text);
    this.text += W;
  }
  delete(k) {
    this.previousStates.push(this.text);
    this.text = this.text.slice(0, this.text.length - k);
  }
  print(k) {
    console.log(this.text[k - 1]);
  }
  undo() {
    this.text = this.previousStates.pop();
  }
}

function processData(input) {
  const queries = input.split("\n").slice(1);
  const textEditor = new TextEditor();

  for (let idx in queries) {
    const query = queries[idx];

    if (query[0] === "1") {
      textEditor.append(query.slice(2));
    } else if (query[0] === "2") {
      textEditor.delete(+query.slice(2));
    } else if (query[0] === "3") {
      textEditor.print(+query.slice(2));
    } else if (query[0] === "4") {
      textEditor.undo();
    }
  }
}
