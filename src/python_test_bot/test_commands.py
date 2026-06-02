from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import asyncio

from python_test_bot.utils.states import DefaultStates

# Construct router
router = Router()


@router.message(Command("start"), StateFilter(None))
async def cmd_start_nonactive(message: Message, state: FSMContext):
    # Start from not active
    await state.set_state(DefaultStates.active)
    await message.answer("Successfully launched")


@router.message(Command("start"), StateFilter(DefaultStates.active))
async def cmd_start_active(message: Message, state: FSMContext):
    # Start if already started
    await message.answer("✅ Already started")


@router.message(Command("stop"), ~StateFilter(None))
async def cmd_stop(message: Message, state: FSMContext):
    # Stop command
    await state.set_state(None)
    await message.answer("🤖 Bot stopped")


@router.message(Command("test"), ~StateFilter(None))
async def cmd_test(message: Message):
    # Command for checking bot still work
    await message.answer("👾")


@router.message(StateFilter(DefaultStates.active))
async def repeat_messages(message: Message):
    # Repeat user message
    # ( One more lay of see if server works)
    await message.reply(str(message.text))
