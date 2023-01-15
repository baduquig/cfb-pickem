import mongoose from 'mongoose';
import Pick from '../models/picks';

export const getAllPicks = async (req, res) => {
    try {
        const pick = await Pick.find();
        res.status(200).json(pick);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}

export const getUserPicks = async (req, res) => {
    const { id } = req.params;
    try {
        const pick = await Pick.findById(id);
        res.status(200).json(pick);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}

export const updatePick = async (req, res) => {
    const { id } = req.params;
    const { userName, schoolPicked, scoreDifferential, points, week, day, date, gameTime, 
            finalScore, awaySchoolId, awaySchoolName, awaySchoolMascot, homeSchoolId, 
            homeSchoolName, homeSchoolMascot, createdDateTime, lastUpdatedDateTime } = req.body;
    
    if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(404).send(`Record not found`);
    } else {
        const updatedPick = { _id: id, userName, schoolPicked, scoreDifferential, points, week, day, date, gameTime, 
                                finalScore, awaySchoolId, awaySchoolName, awaySchoolMascot, homeSchoolId, 
                                homeSchoolName, homeSchoolMascot, createdDateTime, lastUpdatedDateTime }
        await Pick.findByIdAndUpdate(id, updatedPick);
        res.status(200).json(updatedPick);
    }
}