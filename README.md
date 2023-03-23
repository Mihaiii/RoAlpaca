<p align="center" width="100%">
<img src="assets/cabrita.png" alt="Cabrita" style="width: 20%; min-width: 300px; display: block; margin: auto;">
</p>

# RoAlpaca: A romanian finetuned instruction LLaMA

This repository is intended to share all the steps and resources that we used to finetune our version of LLaMA.

This model is designed for research use only, i.e., cannot be used for commercial purposes or entertainment.


## References

> If I have seen further it is by standing on the sholders [sic] of Giants.
> -- <cite>Isaac Newton</cite>

We started this section with this citation because everything we did was only possible due to the strong community and works that other people and groups did. For our work, we rely mainly in the works developed by: [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca Lora](https://github.com/tloen/alpaca-lora), [ChatGPT](https://openai.com/blog/chatgpt) and [Hugging Face](https://huggingface.co/). So, thank you all for the great work and open this to the world!


## Data

We translated the [alpaca_data.json](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json) to romanian using ChatGPT. Even this translation was not the best, the tradeoff between costs and results were. We paid around US$ ??? TBD to translate the full dataset to portuguese.
If you want to know more about how the dataset was built go to: [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca).


## Finetuning

To finetuned the LLaMA model we used the code available on [Alpaca Lora](https://github.com/tloen/alpaca-lora), which provides code to finetune the LLaMA model using PEFT from Hugging Face. With this, we could run our finetuning step using 1 A100 at Colab on top of LLaMA-7B. We trained during TBD hour and we found the results pretty incredible with just that much time. The notebook we used is avaible [here](notebooks/train_lora.ipynb).


## Example outputs
TODO

You can test it using the eval notebook TBD 

## Next steps

- Create a better romanian dataset
- Evaluate the toxicity
- Finetune large models


## Authors

- [Mihaiii](https://github.com/Mihaiii)
- [AndreiXYZ](https://github.com/AndreiXYZ)
- [Felix](https://github.com/TheVexy)
