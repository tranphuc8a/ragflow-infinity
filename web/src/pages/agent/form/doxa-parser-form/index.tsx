import { RAGFlowFormItem } from '@/components/ragflow-form';
import { Form } from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { Textarea } from '@/components/ui/textarea';
import { zodResolver } from '@hookform/resolvers/zod';
import { memo } from 'react';
import { useForm } from 'react-hook-form';
import { useTranslation } from 'react-i18next';
import { z } from 'zod';
import {
  initialDoxaParserValues,
} from '../../constant/pipeline';
import { useFormValues } from '../../hooks/use-form-values';
import { useWatchFormChange } from '../../hooks/use-watch-form-change';
import { INextOperatorForm } from '../../interface';
import { buildOutputList } from '../../utils/build-output-list';
import { FormWrapper } from '../components/form-wrapper';
import { Output } from '../components/output';

export const FormSchema = z.object({
  file_path: z.string().min(1, 'File path is required'),
  doxa_token: z.string().optional(),
  doxa_url: z.string().optional(),
  doxa_ipaas_token: z.string().optional(),
  parse_method: z.string().optional(),
  language: z.string().optional(),
});

export type DoxaParserFormSchemaType = z.infer<typeof FormSchema>;

const outputList = buildOutputList(initialDoxaParserValues.outputs);

const DoxaParserForm = ({ node }: INextOperatorForm) => {
  const defaultValues = useFormValues(initialDoxaParserValues, node);
  const { t } = useTranslation();

  const form = useForm<DoxaParserFormSchemaType>({
    defaultValues,
    resolver: zodResolver(FormSchema),
  });

  useWatchFormChange(node?.id, form);

  return (
    <Form {...form}>
      <FormWrapper>
        {/* File Path Input */}
        <RAGFlowFormItem
          label={t('flow.filePath') || 'File Path'}
          name="file_path"
          tooltip={t('flow.filePathTooltip') || 'Path to the file or variable reference'}
        >
          {(field) => (
            <Input
              placeholder={t('flow.filePathPlaceholder') || 'e.g., /path/to/file.pdf or {{variable}}'}
              {...field}
            />
          )}
        </RAGFlowFormItem>

        {/* DoXA Token */}
        <RAGFlowFormItem
          label={t('flow.doxaToken') || 'DoXA API Token'}
          name="doxa_token"
          tooltip={t('flow.doxaTokenTooltip') || 'DoXA API authentication token (optional, uses DOXA_API_TOKEN env var if not set)'}
        >
          {(field) => (
            <Input
              placeholder={t('flow.doxaTokenPlaceholder') || 'Your DoXA API token'}
              type="password"
              {...field}
            />
          )}
        </RAGFlowFormItem>

        {/* DoXA URL */}
        <RAGFlowFormItem
          label={t('flow.doxaUrl') || 'DoXA API Base URL'}
          name="doxa_url"
          tooltip={t('flow.doxaUrlTooltip') || 'DoXA API endpoint URL (optional, uses DOXA_API_BASE env var if not set)'}
        >
          {(field) => (
            <Input
              placeholder={t('flow.doxaUrlPlaceholder') || 'https://api.doxa-example.com'}
              {...field}
            />
          )}
        </RAGFlowFormItem>

        {/* DoXA iPaaS Token */}
        <RAGFlowFormItem
          label={t('flow.doxaIpaasToken') || 'DoXA iPaaS Token'}
          name="doxa_ipaas_token"
          tooltip={t('flow.doxaIpaasTokenTooltip') || 'Private gateway token for iPaaS deployment (optional)'}
        >
          {(field) => (
            <Input
              placeholder={t('flow.doxaIpaasTokenPlaceholder') || 'Your iPaaS token'}
              type="password"
              {...field}
            />
          )}
        </RAGFlowFormItem>

        {/* Parse Method */}
        <RAGFlowFormItem
          label={t('flow.doxaParseMethod') || 'Parse Method'}
          name="parse_method"
          tooltip={t('flow.doxaParseMethodTooltip') || 'Parsing method to use'}
        >
          {(field) => (
            <Select value={field.value} onValueChange={field.onChange}>
              <SelectTrigger>
                <SelectValue placeholder={t('flow.selectParseMethod') || 'Select parse method'} />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="default">Default</SelectItem>
                <SelectItem value="fast">Fast</SelectItem>
                <SelectItem value="accurate">Accurate</SelectItem>
              </SelectContent>
            </Select>
          )}
        </RAGFlowFormItem>

        {/* Language */}
        <RAGFlowFormItem
          label={t('flow.language') || 'Language'}
          name="language"
          tooltip={t('flow.languageTooltip') || 'Document language for context'}
        >
          {(field) => (
            <Select value={field.value} onValueChange={field.onChange}>
              <SelectTrigger>
                <SelectValue placeholder={t('flow.selectLanguage') || 'Select language'} />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="Chinese">Chinese (简体中文)</SelectItem>
                <SelectItem value="English">English</SelectItem>
                <SelectItem value="Spanish">Spanish (Español)</SelectItem>
                <SelectItem value="French">French (Français)</SelectItem>
                <SelectItem value="German">German (Deutsch)</SelectItem>
                <SelectItem value="Japanese">Japanese (日本語)</SelectItem>
                <SelectItem value="Korean">Korean (한국어)</SelectItem>
                <SelectItem value="Vietnamese">Vietnamese (Tiếng Việt)</SelectItem>
              </SelectContent>
            </Select>
          )}
        </RAGFlowFormItem>

        {/* Output */}
        <Output list={outputList} />
      </FormWrapper>
    </Form>
  );
};

export default memo(DoxaParserForm);
