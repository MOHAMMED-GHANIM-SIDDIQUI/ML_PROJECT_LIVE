from diabetes_predictor.predictor import predict_diabetes


if __name__ == "__main__":
    sample_input = (5, 166, 72, 19, 175, 25.8, 0.587, 51)
    print(predict_diabetes(sample_input))
