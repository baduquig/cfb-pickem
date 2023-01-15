import Pick from '../models/picks';

export const getAllPicks = async (req, res) => {
    try {
        const pick = await Pick.find();
        res.status(200).json(pick);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}