ALGO=$1
ENV=$2
NETWORK=$3
SAVE_DIR=$4

python3 -m baselines.run --alg=$ALGO --env=$ENV --network=$NETWORK --num_timesteps=0 --load_path=./models/$SAVE_DIR --play
