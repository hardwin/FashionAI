import replicate

input = {
    "garm_img": "https://replicate.delivery/pbxt/KgwTlZyFx5aUU3gc5gMiKuD5nNPTgliMlLUWx160G4z99YjO/sweater.webp",
    "human_img": "https://replicate.delivery/pbxt/KgwTlhCMvDagRrcVzZJbuozNJ8esPqiNAIJS3eMgHrYuHmW4/KakaoTalk_Photo_2024-04-04-21-44-45.png",
    "garment_des": "cute pink top"
}

output = replicate.run(
    "cuuupid/idm-vton:f691846e24fc042e3c48483a3ef93762c704371554600d1279729627387c65d8",
    input=input
)
print(output)
#=> "https://replicate.delivery/pbxt/Tfs5JETdzlURKyKeUOltKwch...
