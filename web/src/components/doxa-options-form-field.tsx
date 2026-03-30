import { RAGFlowFormItem } from '@/components/ragflow-form';
import { Input } from '@/components/ui/input';
import { useFormContext, useWatch } from 'react-hook-form';
import { useTranslation } from 'react-i18next';

export function DoxaOptionsFormField({
  namePrefix = 'parser_config',
  parserMethodFieldName = 'parser_config.layout_recognize',
}: {
  namePrefix?: string;
  parserMethodFieldName?: string;
}) {
  const form = useFormContext();
  const { t } = useTranslation();
  const buildName = (field: string) =>
    namePrefix ? `${namePrefix}.${field}` : field;

  const parserMethod = useWatch({
    control: form.control,
    name: parserMethodFieldName,
  });

  const isDoxaSelected =
    parserMethod === 'DoXA' ||
    parserMethod?.toLowerCase?.() === 'doxa';

  if (!isDoxaSelected) {
    return null;
  }

  return (
    <div className="space-y-4 border-l-2 border-primary/30 pl-4 ml-2">
      <div className="text-sm font-medium text-text-secondary">
        {t('knowledgeConfiguration.doxaOptions', 'DoXA options')}
      </div>

      <RAGFlowFormItem
        name={buildName('doxa_url')}
        label={t('knowledgeConfiguration.doxaApiBase', 'DoXA API base URL')}
        tooltip={t(
          'knowledgeConfiguration.doxaApiBaseTip',
          'Base URL for DoXA API service.',
        )}
        horizontal={true}
      >
        {(field) => (
          <Input
            {...field}
            placeholder={t(
              'knowledgeConfiguration.doxaApiBasePlaceholder',
              'e.g. https://api.doxa.example.com',
            )}
          />
        )}
      </RAGFlowFormItem>

      <RAGFlowFormItem
        name={buildName('doxa_token')}
        label={t('knowledgeConfiguration.doxaApiToken', 'DoXA API token')}
        tooltip={t(
          'knowledgeConfiguration.doxaApiTokenTip',
          'Token used to authenticate with DoXA API.',
        )}
        horizontal={true}
      >
        {(field) => (
          <Input
            {...field}
            type="password"
            placeholder={t(
              'knowledgeConfiguration.doxaApiTokenPlaceholder',
              'Input DoXA token (optional if env configured)',
            )}
          />
        )}
      </RAGFlowFormItem>

      <RAGFlowFormItem
        name={buildName('doxa_ipaas_token')}
        label={t('knowledgeConfiguration.doxaIpaasToken', 'DoXA iPaaS token')}
        tooltip={t(
          'knowledgeConfiguration.doxaIpaasTokenTip',
          'Optional iPaaS token for DoXA private gateway.',
        )}
        horizontal={true}
      >
        {(field) => (
          <Input
            {...field}
            type="password"
            placeholder={t(
              'knowledgeConfiguration.doxaIpaasTokenPlaceholder',
              'Input iPaaS token (optional)',
            )}
          />
        )}
      </RAGFlowFormItem>
    </div>
  );
}
