from dataset_creation.dataset_creation_utils import prep_src_data, create_dataset
from train_demo_utils import train_model_const, check_model_const
from transfer_learning.mars_processing import MarsSamples


if __name__ == "__main__":
    # Creation of Mars samples
    ms = MarsSamples(no_samples=8000)
    ms.example_temp()
    # Creation of Moon dataset and model training
    # prep_src_data(open_7zip=False, split_catalogue=False, create_masks=False)
    # create_dataset(no_samples_train=10, no_samples_valid=10, no_samples_test=10, clear_past=True)
    # train_model_const()
