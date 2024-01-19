import os
import logging
from d4kms_generic.logger import application_logger

def test_default_level(caplog):
  assert application_logger.logger.getEffectiveLevel() == logging.DEBUG

def test_debug(caplog):
  application_logger.debug("LOGGING MESSAGE")
  for record in caplog.records:
    assert record.levelname == "DEBUG"
  assert "LOGGING MESSAGE" in caplog.text

def test_info(caplog):
  application_logger.info("LOGGING MESSAGE")
  for record in caplog.records:
    assert record.levelname == "INFO"
  assert "LOGGING MESSAGE" in caplog.text

def test_warning(caplog):
  application_logger.warning("LOGGING MESSAGE")
  for record in caplog.records:
    assert record.levelname == "WARNING"
  assert "LOGGING MESSAGE" in caplog.text

def test_error(caplog):
  application_logger.error("LOGGING MESSAGE")
  for record in caplog.records:
    assert record.levelname == "ERROR"
  assert "LOGGING MESSAGE" in caplog.text

def test_exception(caplog):
  try:
    result = 12 / 0
  except Exception as e:
    application_logger.exception("Divide by zero", e)
  for record in caplog.records:
    assert record.levelname == "ERROR"
  assert "Divide by zero" in caplog.text
