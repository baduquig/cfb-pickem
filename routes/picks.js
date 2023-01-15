import express from 'express';
import * as controllers from '../controllers/picks';

const router = express.Router();

router.get(controllers.getAllPicks());
router.get('/:id', controllers.getUserPicks());
router.patch('/:id', controllers.updatePick());