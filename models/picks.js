import mongoose from "mongoose";

const pickSchema = mongoose.Schema({
    // Pick related data
    _id: {
        userId: Number,
        gameId: Number
    },
    userName: String,
    schoolPicked: {
        type: Number,
        default: ''
    },
    scoreDifferential: {
        type: String,
        default: ''
    },
    points: {
        type: String,
        default: 0
    },
    
    // Game related data
    week: Number,
    day: Number,
    date: String,
    gameTime: Date,
    finalScore: String,
    awaySchoolId: Number,
    awaySchoolName: String,
    awaySchoolMascot: String,
    homeSchoolId: Number,
    homeSchoolName: String,
    homeSchoolMascot: String,

    // Timestamps
    createdDateTime: {
        type: Date,
        default: new Date()
    },
    lastUpdatedDateTime: Date
})

const Pick = mongoose.model('Pick', pickSchema);

export default Pick;