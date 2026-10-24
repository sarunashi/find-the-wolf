import streamlit as st
import random

st.title("ChatGPT と探偵になろう")

# 狼の位置を決める
if "wolf" not in st.session_state:
    st.session_state.wolf = (
        random.randint(0, 4),
        random.randint(0, 4)
    )

wolf_row, wolf_col = st.session_state.wolf

# セリフと画像を表示する場所
picture = st.empty()
message = st.empty()

picture.image("koyagi1.png", width=180)
message.write("さあ、狼はどこかな？")

# 5×5のマスをつくる
for row in range(5):
    cols = st.columns(5)

    for col in range(5):
        if cols[col].button("🐐", key=f"{row}-{col}"):

            # 行の差 + 列の差
            distance = abs(row - wolf_row) + abs(col - wolf_col)

            if distance == 0:
                picture.image("ookami.png", width=180)
                message.write("このあたりにオオカミはいないようだよ。")

            else:
                if distance == 1:
                    picture.image("koyagi3.png", width=180)
                    message.write("こわいよ、近くにいる！")

                elif distance == 2:
                    picture.image("koyagi2.png", width=180)
                    message.write("なんだかイヤな感じがする……。")

                else:
                    picture.image("koyagi1.png", width=180)
                    message.write("このあたりにオオカミはいないようだよ。")