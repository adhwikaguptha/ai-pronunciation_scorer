function ScoreCard({

    score,

    accuracy,

    language,

    languageProbability

}) {

    return (

        <div className="card">

            <h2>Pronunciation Result</h2>

            <div className="score-grid">

                <div className="score-item">

                    <h3>Score</h3>

                    <p>{score}/100</p>

                </div>

                <div className="score-item">

                    <h3>Accuracy</h3>

                    <p>{accuracy}%</p>

                </div>

                <div className="score-item">

                    <h3>Language</h3>

                    <p>{language.toUpperCase()}</p>

                </div>

                <div className="score-item">

                    <h3>Language Confidence</h3>

                    <p>{(languageProbability * 100).toFixed(1)}%</p>

                </div>

            </div>

        </div>

    );

}

export default ScoreCard;