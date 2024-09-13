from factscore import FActScore
import nltk
import os
import json
nltk.download('punkt_tab')

if __name__ == "__main__":
    all_result = []
    file_list = ["plagiarism_200.json","llama3_q_0902.json","t5_base_q_200.json","vec2text_uw_200.json"]
    out = "out"
    for i in range(3):
        result = []
        for file in file_list:
            rst = []
            file_path = os.path.join(out, file) 
            with open(file_path,'r') as f:
                data = json.load(f)
            predictions = [data[i]["prediction"]]
            targets = [data[i]["target"]]
            strict_list = ["strict","moderate","loose"]
            for strictness in strict_list:
                fs = FActScore(strictness=strictness,case=i,file=file)
                scores = fs.compute(predictions, targets)
                print(f"{file}:{strictness}:\nscores:{scores}")
                rst.append({
                    "strictness":strictness,
                    "score":scores,
                })
            tmp = {
                "file":file,
                "target": targets[0],
                "prediction": predictions[0],
                "score_list":rst,
            }
            result.append(tmp)
        rst_file = f"score/case_{i}"
        with open(rst_file,'w') as f:
            json.dump(result, f, indent=4)
