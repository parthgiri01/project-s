"""
train_all.py
============
Run this from the project root to train all models in one command:

    python train_all.py                   # uses synthetic demo data
    python train_all.py --train data/KDDTrain+.txt --test data/KDDTest+.txt
"""

import sys
import os

# Make sure src/ is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import joblib
import argparse
from preprocess import get_data
from train import train_all
from evaluate import evaluate_all

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODEL_DIR, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Train + evaluate all IDS models")
    parser.add_argument("--train", default=None,
                        help="NSL-KDD train file path")
    parser.add_argument("--test",  default=None,
                        help="NSL-KDD test file path")
    parser.add_argument("--demo",  action="store_true",
                        help="Force use of synthetic demo data")
    args = parser.parse_args()

    use_demo = args.demo or (args.train is None)

    print("=" * 60)
    print("  ML-Based Intrusion Detection System — Training Pipeline")
    print("=" * 60)

    # 1. Load & preprocess data
    X_train, X_test, y_train, y_test, scaler, encoders = get_data(
        train_path=args.train,
        test_path=args.test,
        demo=use_demo,
    )

    # 2. Save shared artifacts
    joblib.dump(scaler,   os.path.join(MODEL_DIR, "scaler.pkl"))
    joblib.dump(encoders, os.path.join(MODEL_DIR, "encoders.pkl"))
    print("[SAVE]  scaler.pkl + encoders.pkl saved.")

    # 3. Train all models
    trained = train_all(X_train, y_train, demo=use_demo)

    # 4. Evaluate all models
    print("\n[EVAL]  Evaluating all models …")
    results = evaluate_all(X_test, y_test, demo=use_demo)

    best = results.iloc[0]["model"]
    print(f"\n✅  Best model: {best}  "
          f"(Accuracy: {results.iloc[0]['accuracy']:.1%})")
    print("\nTraining complete. Run the dashboard with:")
    print("  cd dashboard && python app.py")


if __name__ == "__main__":
    main()
