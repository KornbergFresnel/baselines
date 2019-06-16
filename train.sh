LOG_NAME=$1
ALGO=$2
ENV=$3
NETWORK=$4
SAVE_DIR=$5

OPENAI_LOGDIR=./logs/$LOG_NAME python -m baselines.run --alg=$ALGO --env=$ENV --network=$NETWORK --save_path=./models/$SAVE_DIR --num_timesteps=2e7
