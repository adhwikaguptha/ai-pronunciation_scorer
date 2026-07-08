function AnalysisTable({ analysis }) {

    if (!analysis || analysis.length === 0) {

        return (

            <div className="card">

                <h2>Pronunciation Issues</h2>

                <p>No pronunciation issues detected. Great job! 🎉</p>

            </div>

        );

    }

    return (

        <div className="card">

            <h2>Pronunciation Issues</h2>

            <table>

                <thead>

                    <tr>

                        <th>Expected</th>

                        <th>Recognized</th>

                        <th>Status</th>

                        <th>Similarity</th>

                    </tr>

                </thead>

                <tbody>

                    {analysis.map((item, index) => (

                        <tr key={index}>

                            <td>{item.expected || "-"}</td>

                            <td>{item.spoken || "-"}</td>

                            <td>{item.status}</td>

                            <td>

                                {item.similarity !== undefined
                                    ? `${item.similarity}%`
                                    : "-"}

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default AnalysisTable;