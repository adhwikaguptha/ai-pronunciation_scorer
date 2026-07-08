function FeedbackList({ feedback }) {

    if (!feedback || feedback.length === 0) {

        return null;

    }

    return (

        <div className="card">

            <h2>Feedback</h2>

            {

                feedback.map((item, index) => (

                    <div
                        key={index}
                        style={{ marginBottom: "25px" }}
                    >

                        <h3>{item.title}</h3>

                        {

                            item.words.length > 0 && (

                                <ul>

                                    {

                                        item.words.map((word, i) => (

                                            <li key={i}>

                                                {word}

                                            </li>

                                        ))

                                    }

                                </ul>

                            )

                        }

                        <p>{item.message}</p>

                        <hr />

                    </div>

                ))

            }

        </div>

    );

}

export default FeedbackList;