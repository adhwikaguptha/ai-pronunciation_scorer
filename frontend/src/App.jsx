import { useState } from "react";

import UploadAudio from "./components/UploadAudio";
import ScoreCard from "./components/ScoreCard";
import Transcript from "./components/Transcript";
import AnalysisTable from "./components/AnalysisTable";
import FeedbackList from "./components/FeedbackList";

import "./index.css";

function App() {

  const [result, setResult] = useState(null);

  return (

    <div className="container">

      <h1> AI Pronunciation Analyzer</h1>

      <p className="subtitle">
        Upload a 30–45 second English audio clip and compare it with the reference text.
      </p>

      <UploadAudio setResult={setResult} />

      {result && (

        <>

          <ScoreCard
            score={result.score}
            accuracy={result.accuracy}
            language={result.language}
            languageProbability={result.language_probability}
          />

          <Transcript
            reference={result.reference_text}
            transcript={result.transcript}
          />

          <AnalysisTable
            analysis={result.analysis}
          />

          <FeedbackList
            feedback={result.feedback}
          />

        </>

      )}

    </div>

  );

}

export default App;